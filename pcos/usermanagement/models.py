from django.db import models
from django.contrib.auth.models import AbstractUser

#table creation
class Register(AbstractUser):
    place=models.CharField(max_length=50,null=True)
    contact=models.IntegerField(default=0,null=True)
    userType=models.CharField(max_length=50,default="admin")




class Feedback(models.Model):
    experience=models.CharField(max_length=50,null=True)
    comments=models.CharField(max_length=100,null=True)
    Date_submitted=models.DateField(null=True)
    user_id=models.ForeignKey(Register,on_delete=models.CASCADE,null=True)



    



