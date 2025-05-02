from django import forms
from .models import *


class PCOSPredictionForm(forms.ModelForm):
    AGE_CHOICES = [(i, i) for i in range(10, 100)]
    BLOOD_GROUP_CHOICES = [
        ('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'),
        ('O+', 'O+'), ('O-', 'O-'), ('AB+', 'AB+'), ('AB-', 'AB-')
    ]
    BOOLEAN_CHOICES = [(1, 'Yes'), (0, 'No')]

    # Form Fields with CSS Styling
    age = forms.ChoiceField(choices=AGE_CHOICES, label="Age (yrs)", widget=forms.Select(attrs={'class': 'form-control'}))
    weight = forms.FloatField(label="Weight (Kg)", widget=forms.NumberInput(attrs={'class': 'form-control'}))
    height = forms.FloatField(label="Height (Cm)", widget=forms.NumberInput(attrs={'class': 'form-control'}))
    bmi = forms.FloatField(label="BMI", widget=forms.NumberInput(attrs={'class': 'form-control'}))
    blood_group = forms.ChoiceField(choices=BLOOD_GROUP_CHOICES, label="Blood Group", widget=forms.Select(attrs={'class': 'form-control'}))
    pulse_rate = forms.IntegerField(label="Pulse Rate (bpm)", widget=forms.NumberInput(attrs={'class': 'form-control'}))
    rr = forms.IntegerField(label="Respiratory Rate (breaths/min)", widget=forms.NumberInput(attrs={'class': 'form-control'}))
    cycle_length = forms.IntegerField(label="Cycle Length (days)", widget=forms.NumberInput(attrs={'class': 'form-control'}))
    marriage_status = forms.IntegerField(label="Marriage Status (Years)", widget=forms.NumberInput(attrs={'class': 'form-control'}))
    pregnant = forms.ChoiceField(choices=BOOLEAN_CHOICES, label="Pregnant", widget=forms.Select(attrs={'class': 'form-control'}))
    hip = forms.FloatField(label="Hip (inch)", widget=forms.NumberInput(attrs={'class': 'form-control'}))
    waist = forms.FloatField(label="Waist (inch)", widget=forms.NumberInput(attrs={'class': 'form-control'}))
    waist_hip_ratio = forms.FloatField(label="Waist:Hip Ratio", widget=forms.NumberInput(attrs={'class': 'form-control'}))
    weight_gain = forms.ChoiceField(choices=BOOLEAN_CHOICES, label="Weight Gain", widget=forms.Select(attrs={'class': 'form-control'}))
    hair_growth = forms.ChoiceField(choices=BOOLEAN_CHOICES, label="Hair Growth", widget=forms.Select(attrs={'class': 'form-control'}))
    skin_darkening = forms.ChoiceField(choices=BOOLEAN_CHOICES, label="Skin Darkening", widget=forms.Select(attrs={'class': 'form-control'}))
    hair_loss = forms.ChoiceField(choices=BOOLEAN_CHOICES, label="Hair Loss", widget=forms.Select(attrs={'class': 'form-control'}))
    pimples = forms.ChoiceField(choices=BOOLEAN_CHOICES, label="Pimples", widget=forms.Select(attrs={'class': 'form-control'}))
    fast_food = forms.ChoiceField(choices=BOOLEAN_CHOICES, label="Fast Food Consumption", widget=forms.Select(attrs={'class': 'form-control'}))
    regular_exercise = forms.ChoiceField(choices=BOOLEAN_CHOICES, label="Regular Exercise", widget=forms.Select(attrs={'class': 'form-control'}))
    bp_systolic = forms.IntegerField(label="BP Systolic (mmHg)", widget=forms.NumberInput(attrs={'class': 'form-control'}))
    bp_diastolic = forms.IntegerField(label="BP Diastolic (mmHg)", widget=forms.NumberInput(attrs={'class': 'form-control'}))
    class Meta:
        model=PCOSPrediction
        fields = ['age','weight','height','bmi','blood_group','pulse_rate','rr','cycle_length','marriage_status','pregnant','hip','waist','waist_hip_ratio','weight_gain','hair_growth','skin_darkening','hair_loss','pimples','fast_food','regular_exercise','bp_systolic','bp_diastolic']


class ImageUploadForm(forms.Form):
    image = forms.ImageField(label='Upload Image')