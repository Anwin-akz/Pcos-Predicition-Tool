from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
import os
import numpy as np
# import cv2
# import tensorflow as tf

# Load the trained model
# MODEL_PATH = os.path.join(os.path.dirname(__file__), 'full_model.h5')
# model = tf.keras.models.load_model(MODEL_PATH)

# # Define image size expected by the model
# IMAGE_SIZE = (224, 224)

# def preprocess_image(image_path):
#     img = cv2.imread(image_path)
#     img = cv2.resize(img, IMAGE_SIZE)
#     img = img / 255.0  # Normalize
#     img = np.expand_dims(img, axis=0)  # Add batch dimension
#     return img

# def predict_pcos(request):
#     if request.method == 'POST':
#         form = ImageUploadForm(request.POST, request.FILES)
#         if form.is_valid():
#             image_file = request.FILES['image']
#             file_path = default_storage.save('uploads/' + image_file.name, ContentFile(image_file.read()))
#             file_full_path = os.path.join(default_storage.location, file_path)
           
#             # Preprocess and predict
#             processed_image = preprocess_image(file_full_path)
#             prediction = model.predict(processed_image)[0]
           
#             # Assuming binary classification (0 = No PCOS, 1 = PCOS)
#             result = "PCOS Detected" if prediction[1] > prediction[0] else "No PCOS Detected"
           
#             return render(request, 'result.html', {'form': form, 'image_url': file_path, 'result': result})
#     else:
#         form = ImageUploadForm()
#     return render(request, 'image_upload', {'form': form})
