from django.shortcuts import render
import os
import numpy as np
import pandas as pd
import joblib

# Load the trained model
# MODEL_PATH = os.path.join(os.path.dirname(__file__), 'random_forest_model.pkl')
# model = joblib.load(MODEL_PATH)

# # Define the input features used by the model
# FEATURES = ['Age', 'BMI', 'Cycle Length', 'Irregular Periods', 'Hair Growth', 'Acne', 'Weight Gain', 'Infertility']

# def predict_pcos(request):
#     if request.method == 'POST':
#         form = PCOSDiagnosisForm(request.POST)
#         if form.is_valid():
#             input_data = pd.DataFrame([form.cleaned_data], columns=FEATURES)
#             prediction = model.predict(input_data)[0]
#             probability = model.predict_proba(input_data)[0][1]  # Probability of having PCOS
           
#             result = "PCOS Detected" if prediction == 1 else "No PCOS Detected"
#             recommendations = "Maintain a healthy diet and consult a specialist for further diagnosis." if prediction == 1 else "Your results are normal, but it's good to have routine checkups."
           
#             return render(request, 'result.html', {'form': form, 'result': result, 'probability': probability, 'recommendations': recommendations})
#     else:
#         form = PCOSDiagnosisForm()
#     return render(request, 'diagnosis.html', {'form': form})
