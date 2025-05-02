from django import forms
from .models import *



class RegisterForm(forms.ModelForm):
    class Meta:
        model=Register
        fields=['username','email','password','first_name','last_name']
        help_texts={
            'username':None,
            # 'password':'The password should contain 6 digits and 1 letter'
        }






class LoginForm(forms.ModelForm):
    class Meta:
        model=Register
        fields=['username','password']
        help_texts={
            'username':None,
            'password':None,
        }




class FeedbackForm(forms.ModelForm):
    class Meta:
        model=Feedback
        fields=['experience','comments']
        # help_texts={
        #     'username':'',
        #     # 'password':'The password should contain 6 digits and 1 letter'
        # }