import cv2
import time
import os
import requests
from zipfile import ZipFile
from datetime import datetime

camera_url = "http://192.168.121.128:81/stream"  # ESP32-CAM stream URL
capture_folder = "captured_images"
zip_file_path = "images.zip"
backend_url = "http://127.0.0.1:8000/api/predict/"  # Replace with your backend prediction API URL

# Ensure the capture folder exists
if not os.path.exists(capture_folder):
    os.makedirs(capture_folder)

def connect_to_camera():
    """Attempt to connect to the camera with retries."""
    retries = 5
    while retries > 0:
        cap = cv2.VideoCapture(camera_url)
        cap.set(cv2.CAP_PROP_BUFFERSIZE, 1)  # Minimize buffer size
        cap.set(cv2.CAP_PROP_FPS, 30)  # Set FPS
        if cap.isOpened():
            print("Camera connection successful.")
            return cap
        else:
            print(f"Error: Unable to connect to the camera. Retrying... ({retries} attempts left)")
            retries -= 1
            time.sleep(5)
    print("Failed to connect to the camera after multiple attempts.")
    return None

def delete_files(folder, zip_file):
    """Delete captured images and ZIP file."""
    # Delete captured images
    try:
        for filename in os.listdir(folder):
            file_path = os.path.join(folder, filename)
            os.remove(file_path)
            
    except Exception as e:
        print(f"Error deleting captured images: {e}")

    # Delete the ZIP file
    try:
        if os.path.exists(zip_file):
            os.remove(zip_file)
            print(f"Deleted ZIP file: {zip_file}")
    except Exception as e:
        print(f"Error deleting ZIP file: {e}")

# Connect to the camera
cap = connect_to_camera()
if cap is not None:
    try:
        # Capture images for 30 seconds
        start_time = time.time()
        end_time = start_time + 30  # Capture for 30 seconds
        count = 0

        while time.time() < end_time:
            ret, frame = cap.read()
            if ret:
                filename = f"{capture_folder}/image_{count}.jpg"
                success = cv2.imwrite(filename, frame)
                if success:
                    print(f"Captured: {filename}")
                else:
                    print(f"Error: Failed to save {filename}")
                count += 1
            else:
                print("Warning: Failed to capture an image.")
            time.sleep(1)  # Capture one image per second

        print("Finished capturing 30 seconds of images.")

        # Create a ZIP file of captured images
        with ZipFile(zip_file_path, 'w') as zipf:
            for filename in os.listdir(capture_folder):
                zipf.write(os.path.join(capture_folder, filename), filename)

        print("Images compressed into ZIP file.")

        # Send the ZIP file to the backend
        with open(zip_file_path, 'rb') as zipf:
            print("Sending ZIP file to backend for prediction...")
            response = requests.post(backend_url, files={'file': ('images.zip', zipf, 'application/zip')})
            if response.status_code == 200:
                prediction = response.json()
                print(f"Prediction: {prediction}")

                # Log the prediction with the current date
                current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                print(f"Disease detected: {prediction.get('detected_disease', 'N/A')} on {current_date}")
            else:
                print(f"Backend Error: {response.status_code}, {response.text}")

        # Delete files after processing
        # delete_files(capture_folder, zip_file_path)

    except Exception as e:
        print(f"Error during image capture or processing: {e}")
    
    finally:
        # Release the camera
        cap.release()
        print("Camera connection closed.")
else:
    print("Skipping further steps due to camera connection failure.")
