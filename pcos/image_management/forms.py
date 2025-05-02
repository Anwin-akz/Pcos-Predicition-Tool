from django import forms
from django.urls import path
from .views import predict_pcos

# class ImageUploadForm(forms.Form):
#     image = forms.ImageField(label='Upload Image')