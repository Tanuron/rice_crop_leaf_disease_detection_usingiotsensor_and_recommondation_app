# 🌾 RiceGuard: Rice Disease Detection App

**RiceGuard** is a smart mobile app that identifies rice leaf diseases in real-time. It uses a deep learning model (PyTorch) with a Django backend. The app helps farmers detect diseases early and gives pesticide and care suggestions.

---

## 📸 App Screenshots

<h3>🔐 Authentication Page</h3>

<p align="center">
  <img src="assets/images/sig_in.jpg" alt="Authentication Page" width="400" />
  <img src="assets/images/sign_in_page.jpg" alt="Authentication Page" width="400"/>
</p>

<h3>🏠 Home Page</h3>

<img src="assets/images/home_page.jpg" alt="Home Page" width="400" />


<h3>Camera/image upload</h3>
<img src="assets/images/uploading_image.jpg" alt="Image upload" width="400" />

<h3>Prediction output with confidence</h3>
<img src="assets/images/prediction_page.jpg" alt="prediction" width="400" />

<h3>Disease info and treatment</h3>
<p align="center">
  <img src="assets/images/plant_disease.jpg" width="400" height="650"/>
  <img src="assets/images/pesticides_recomondation.jpg" width="400" />
</p>
<h3>Dashboard</h3>  
<img src="assets/images/dashboard.jpg" alt="dashboard" width="400" />

<h3>Care tips and disease guide</h3>
<img src="assets/images/plant_care_tips.jpg" alt="plant_care_tips" width="400" />



---

## 💡 Features

- 📷 Capture images or upload from gallery  
- 🧠 CNN model detects diseases  
- 🌐 Django backend (REST API)  
- 💬 Gives name, confidence, pesticide, and care tips  
- ☁️ Weather info and IoT integration  
- 🔐 Login & signup support  
- 🪴 Disease prevention dashboard  

---

## 🧠 Model Details

- **Framework**: PyTorch  
- **Type**: CNN (Convolutional Neural Network)  
- **Classes**: Brown Spot, Leaf Blast, Bacterial Blight, Healthy  
- **Augmentations**: Flip, rotate, normalize  
- **Metrics**: Accuracy, Loss  

---

