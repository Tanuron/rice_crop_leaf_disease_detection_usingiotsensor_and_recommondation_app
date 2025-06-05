from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import torch
import torch.nn.functional as F
import torchvision.transforms as transforms
from torchvision.models import resnet50, ResNet50_Weights
from torchvision import datasets
from PIL import Image, UnidentifiedImageError
import logging
import traceback
import json
from .utils import DISEASE_INFO
import zipfile
from collections import defaultdict
from .models import Prediction
# Logger
logger = logging.getLogger(__name__)

# Custom ResNet50 Model
class CustomResNet50(torch.nn.Module):
    def __init__(self, num_classes):
        super(CustomResNet50, self).__init__()
        self.resnet50 = resnet50(weights=ResNet50_Weights.DEFAULT)
        for param in self.resnet50.parameters():
            param.requires_grad = False
        self.resnet50.fc = torch.nn.Linear(self.resnet50.fc.in_features, num_classes)

    def forward(self, x):
        return self.resnet50(x)

# Load your dataset and model
dataset = datasets.ImageFolder(root=r'C:\Users\DELL\Documents\miniproject\RiceLeafDiseaseImages')
class_names = dataset.classes
model = CustomResNet50(num_classes=len(class_names))
model.load_state_dict(torch.load(r"C:\Users\DELL\Documents\rice\models\myresnetmodel.pth", map_location=torch.device('cpu'), weights_only=True))
model.eval()

# Transformation pipeline
transform = transforms.Compose([
    transforms.Resize((556, 556)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
])



# Disease prediction view
@csrf_exempt
def predict(request):
    if request.method == 'POST' and request.FILES.get('file'):
        try:
            file = request.FILES['file']
            logger.info(f"Received file: {file.name}")

            # Check if the file is a ZIP
            if file.name.endswith('.zip'):
                # Handle ZIP file
                with zipfile.ZipFile(file, 'r') as zip_ref:
                    disease_confidences = defaultdict(list)

                    for filename in zip_ref.namelist():
                        try:
                            with zip_ref.open(filename) as image_file:
                                img = Image.open(image_file).convert('RGB')
                                img = transform(img).unsqueeze(0)

                                with torch.no_grad():
                                    output = model(img)

                                probabilities = torch.nn.functional.softmax(output, dim=1)
                                confidence, predicted = torch.max(probabilities, 1)

                                prediction_name = class_names[predicted.item()]
                                confidence_percentage = confidence.item() * 100

                                # Aggregate confidence scores for each disease
                                disease_confidences[prediction_name].append(confidence_percentage)

                        except UnidentifiedImageError:
                            logger.warning(f"Skipping non-image file in ZIP: {filename}")
                        except Exception as e:
                            logger.error(f"Error processing {filename}: {str(e)}", exc_info=True)

                    if not disease_confidences:
                        return JsonResponse({'error': 'No valid images found in the ZIP file.'}, status=400)

                    # Calculate average confidence for each disease
                    averaged_confidences = {
                        disease: sum(confidences) / len(confidences)
                        for disease, confidences in disease_confidences.items()
                    }

                    # Find the disease with the highest average confidence
                    detected_disease = max(averaged_confidences, key=averaged_confidences.get)
                    avg_confidence = averaged_confidences[detected_disease]

                    # Retrieve information for the detected disease
                    disease_info = DISEASE_INFO.get(detected_disease, {})
                    pesticides = disease_info.get("pesticides", [])
                    precautions = disease_info.get("precautions", [])

                    # Store prediction in the database
                    store_prediction_data = {
                        'detected_disease': detected_disease,
                        'average_confidence': avg_confidence,
                        'pesticides': ", ".join(pesticides),
                        'precautions': ", ".join(precautions),
                    }

                    # You can directly create a Prediction object here instead of calling store_prediction
                    Prediction.objects.create(**store_prediction_data)

                    return JsonResponse({
                        'detected_disease': detected_disease,
                        'average_confidence': avg_confidence,
                        'pesticides': pesticides,
                        'precautions': precautions,
                    }, status=200)

            else:
                # Handle single image file
                img = Image.open(file).convert('RGB')
                img = transform(img).unsqueeze(0)

                with torch.no_grad():
                    output = model(img)

                probabilities = torch.nn.functional.softmax(output, dim=1)
                confidence, predicted = torch.max(probabilities, 1)

                prediction_name = class_names[predicted.item()]
                confidence_percentage = confidence.item() * 100

                disease_info = DISEASE_INFO.get(prediction_name, {})
                pesticides = disease_info.get("pesticides", [])
                precautions = disease_info.get("precautions", [])

                # Store the prediction in the database
                store_prediction_data = {
                    'detected_disease': prediction_name,
                    'average_confidence': confidence_percentage,
                    'pesticides': ", ".join(pesticides),
                    'precautions': ", ".join(precautions),
                }

                Prediction.objects.create(**store_prediction_data)

                return JsonResponse({
                    'prediction': prediction_name,
                    'confidence': confidence_percentage,
                    'pesticides': pesticides,
                    'precautions': precautions,
                }, status=200)

        except Exception as e:
            logger.error(f"Prediction error: {str(e)}", exc_info=True)
            return JsonResponse({'error': 'An error occurred during prediction.'}, status=500)

    return JsonResponse({'error': 'Invalid request'}, status=400)


@csrf_exempt
def store_prediction(request, store_prediction_request=None):
    if request.method == 'POST' or store_prediction_request:
        try:
            # If called directly, parse the JSON data from the passed argument
            if store_prediction_request:
                data = json.loads(store_prediction_request)
            else:
                # Parse the JSON data sent by the client
                data = json.loads(request.body)

            detected_disease = data.get('detected_disease')
            average_confidence = data.get('average_confidence')
            pesticides = data.get('pesticides', '')
            precautions = data.get('precautions', '')

            # Validate required fields
            if not detected_disease or average_confidence is None:
                return JsonResponse({'error': 'Missing required fields'}, status=400)

            # Save the prediction to the database
            prediction = Prediction.objects.create(
                detected_disease=detected_disease,
                average_confidence=average_confidence,
                pesticides=pesticides,
                precautions=precautions,
            )

            return JsonResponse({'message': 'Prediction stored successfully', 'id': prediction.id}, status=201)

        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON data'}, status=400)

    return JsonResponse({'error': 'Invalid request method'}, status=405)

def get_predictions(request):
    if request.method == 'GET':
        # Fetch all predictions
        predictions = Prediction.objects.all().values()
        return JsonResponse(list(predictions), safe=False, status=200)
    return JsonResponse({'error': 'Invalid request method'}, status=405)