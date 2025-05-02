from django.db import models
from django.conf import settings
from usermanagement.models import *

class PCOSPrediction(models.Model):
    user = models.ForeignKey(Register, on_delete=models.CASCADE, related_name='pcos_predictions',blank=True)
    age = models.IntegerField(null=True)
    weight = models.FloatField(null=True)
    height = models.FloatField(null=True)
    bmi = models.FloatField(null=True)
    blood_group = models.CharField(max_length=3)
    pulse_rate = models.IntegerField(null=True)
    rr = models.IntegerField(null=True)
    cycle_length = models.IntegerField(null=True)
    marriage_status = models.IntegerField(null=True)
    pregnant = models.BooleanField(default=False)
    hip = models.FloatField(null=True)
    waist = models.FloatField(null=True)
    waist_hip_ratio = models.FloatField(null=True)
    weight_gain = models.BooleanField(default=False)
    hair_growth = models.BooleanField(default=False)
    skin_darkening = models.BooleanField(default=False)
    hair_loss = models.BooleanField(default=False)
    pimples = models.BooleanField(default=False)
    fast_food = models.BooleanField(default=False)
    regular_exercise = models.BooleanField(default=False)
    bp_systolic = models.IntegerField(null=True)
    bp_diastolic = models.IntegerField(null=True)
    prediction = models.CharField(max_length=50,null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.prediction} ({self.created_at})"
