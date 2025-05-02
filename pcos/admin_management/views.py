from .forms import *
from.models import *
import os
import pickle
import json
import random
import joblib
import numpy as np
import cv2
import tensorflow as tf


import pandas as pd
from django.conf import settings
from django.shortcuts import render
from django.http import JsonResponse
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile


# Define paths correctly using Django's BASE_DIR
MODEL_PATH = ('C:/Users/user/Desktop/Anwin/College/project/zuike/PCOS_VENV_3_12_9/pcos/chat_management/model/chatbot_model.pkl')
VECTORIZER_PATH = ('C:/Users/user/Desktop/Anwin/College/project/zuike/PCOS_VENV_3_12_9/pcos/chat_management/model/vectorizer.pkl')
INTENTS_PATH = ('C:/Users/user/Desktop/Anwin/College/project/zuike/PCOS_VENV_3_12_9/pcos/chat_management/dataset/chatdata.json')
print("sjhdfjsdf")
# Load the model and vectorizer once at startup
try:
    with open(MODEL_PATH, 'rb') as f:
        best_model = pickle.load(f)
        print(best_model,"best")
    with open(VECTORIZER_PATH, 'rb') as f:
        vectorizer = pickle.load(f)

    with open(INTENTS_PATH, 'r') as f:
        intents = json.load(f)

except Exception as e:
    best_model, vectorizer, intents = None, None, None
    print(f"Error loading chatbot assets: {e}")

def chatbot_response(user_input):
    if not best_model or not vectorizer or not intents:
        return "Chatbot is not available. Please try again later."

    input_text = vectorizer.transform([user_input])
    predicted_intent = best_model.predict(input_text)[0]

    for intent in intents['intents']:
        if intent['tag'] == predicted_intent:
            return random.choice(intent['responses'])

    return "I'm sorry, I didn't understand that."

def chats(request):
    if request.method == 'POST':
        user_input = request.POST.get('user_input', '')

        response_text = chatbot_response(user_input)
        # print(response_text)

        return JsonResponse({'response_text': response_text})
    else:
        return render(request, 'chat.html')
    



    
def load_model_and_scaler():
    """Load the trained model and scaler from pickle files."""
    with open("C:/Users/user/Desktop/Anwin/PCOS Project/PCOS_VENV_3_12_9/pcos/admin_management/cv_prediction.pkl", "rb") as model_file:
        model = pickle.load(model_file)
    with open("C:/Users/user/Desktop/Anwin/PCOS Project/PCOS_VENV_3_12_9/pcos/admin_management/scaler.pkl", "rb") as scaler_file:
        scaler = pickle.load(scaler_file)
    return model, scaler

def preprocess_input(form_data):
    """Convert user input to numerical format for prediction."""
    blood_group_mapping = {
        'A+': 11, 'A-': 12, 'B+': 13, 'B-': 14, 'O+': 15, 'O-': 16, 'AB+': 17, 'AB-': 18
    }
    # binary_mapping = {1: 1, 0: 0}
    
    processed_data = [
        form_data['age'], form_data['weight'], form_data['height'], form_data['bmi'],
        blood_group_mapping[form_data['blood_group']], form_data['pulse_rate'], form_data['rr'],
        form_data['cycle_length'], form_data['marriage_status'], form_data['pregnant'],
        form_data['hip'], form_data['waist'], form_data['waist_hip_ratio'], form_data['weight_gain'],
        form_data['hair_growth'], form_data['skin_darkening'],
        form_data['hair_loss'], form_data['pimples'],
        form_data['fast_food'], form_data['regular_exercise'],
        form_data['bp_systolic'], form_data['bp_diastolic']
    ]
    return np.array([processed_data])

def predict_pcos(request):
    model, scaler = load_model_and_scaler()
    result, recommendations, diagnosis_summary = None, None, None  

    if request.method == 'POST':
        form = PCOSPredictionForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.user = request.user
            user.save()
            input_df = preprocess_input(form.cleaned_data)
            input_scaled = scaler.transform(input_df)

            # Check if model supports predict_proba()
            if hasattr(model, "predict_proba"):
                proba = model.predict_proba(input_scaled)[:, 1]  # Probability of PCOS
                print("PCOS Probability:", proba[0])  # Debugging output
                threshold = 0.4  # Adjust if necessary
                prediction = 1 if proba[0] >= threshold else 0
            else:
                prediction = model.predict(input_scaled)[0]  # Direct prediction

            print("Raw Prediction:", prediction)  # Debugging output
            result = "PCOS Detected" if prediction == 1 else "No PCOS Detected"

            user.prediction = result
            user.save()

            # **Generate a detailed diagnosis summary**
            summary = []
            form_data = form.cleaned_data  # Extract user inputs

            if form_data['bmi'] >= 25:
                summary.append("Your BMI is in the overweight range, which is a risk factor for PCOS.")
            if form_data['cycle_length'] > 35:
                summary.append("Irregular or long menstrual cycles may indicate hormonal imbalances.")
            if form_data['weight_gain']:
                summary.append("Unexplained weight gain is commonly associated with PCOS.")
            if form_data['hair_growth']:
                summary.append("Excessive hair growth (hirsutism) can be due to elevated androgen levels.")
            if form_data['hair_loss']:
                summary.append("Hair thinning or hair loss may indicate hormonal imbalance.")
            if form_data['pimples']:
                summary.append("Frequent acne breakouts can be linked to excess androgens.")
            if form_data['bp_systolic'] > 130 or form_data['bp_diastolic'] > 85:
                summary.append("Elevated blood pressure levels may increase risks of metabolic issues.")

            diagnosis_summary = " |" \
            " ".join(summary) if summary else "No significant risk factors detected."

            # **Provide Recommendations**
            if prediction == 1:
                recommendations = (
                    "✔ Maintain a healthy diet (low sugar & processed food).\n"
                    "✔ Engage in regular exercise (30 min/day).\n"
                    "✔ Monitor menstrual cycles and hormonal levels.\n"
                    "✔ Consider consulting a gynecologist for further evaluation.\n"
                    "✔ Lifestyle changes can help manage symptoms effectively."
                )
            else:
                recommendations = (
                    "✔ You are at low risk of PCOS.\n"
                    "✔ Maintain a balanced diet and exercise routine.\n"
                    "✔ Stay hydrated and follow up on regular health checkups.\n"
                    "✔ Keep monitoring your menstrual cycle for any irregularities."
                )

    else:
        form = PCOSPredictionForm()

    return render(request, 'prediction.html', {
        'form': form, 
        'result': result, 
        'recommendations': recommendations, 
        'diagnosis_summary': diagnosis_summary
    })


MODEL_PATH = ('C:/Users/user/Desktop/Anwin/College/project/zuike/PCOS_VENV_3_12_9/pcos/admin_management/full_model_1.h5')
model = tf.keras.models.load_model(MODEL_PATH)

# Define image size expected by the model
IMAGE_SIZE = (224, 224)

def preprocess_image(image_path):
    img = cv2.imread(image_path)
    img = cv2.resize(img, IMAGE_SIZE)
    img = img / 255.0  # Normalize
    img = np.expand_dims(img, axis=0)  # Add batch dimension
    return img


from django.http import JsonResponse  # Import JsonResponse

def image_pcos(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            image_file = request.FILES['image']
            file_path = default_storage.save('uploads/' + image_file.name, ContentFile(image_file.read()))
            file_full_path = os.path.join(default_storage.location, file_path)

            # Preprocess and predict
            processed_image = preprocess_image(file_full_path)
            prediction = model.predict(processed_image)[0]  # Output: [No PCOS prob, PCOS prob]

            pcos_prob = prediction[1]  # Probability of PCOS
            no_pcos_prob = prediction[0]  # Probability of No PCOS

            # Determine Result and Severity Level
            if pcos_prob > no_pcos_prob:
                result = "PCOS Detected"

                # Assign severity level based on probability
                if pcos_prob > 0.8:
                    severity = "Severe"
                    suggestion = "Consult a gynecologist immediately. Maintain a healthy diet and consider medications."
                elif pcos_prob > 0.5:
                    severity = "Moderate"
                    suggestion = "Exercise regularly, manage stress, and monitor your diet."
                else:
                    severity = "Mild"
                    suggestion = "Lifestyle modifications like reducing sugar intake and staying active can help."

            else:
                result = "No PCOS Detected"

                # Assign risk level based on probability
                if no_pcos_prob > 0.8:
                    severity = "Low Risk"
                elif no_pcos_prob > 0.5:
                    severity = "Moderate Risk"
                else:
                    severity = "High Risk (Monitor Symptoms)"

                suggestion = "Maintain a balanced lifestyle and monitor symptoms regularly."

            print(result, severity, suggestion)  # Debugging: Check values in the console

            # Return JSON response
            return JsonResponse({'result': result, 'severity': severity, 'suggestion': suggestion})

    # If not a POST request, render the upload form
    form = ImageUploadForm()
    return render(request, 'image_upload.html', {'form': form})
