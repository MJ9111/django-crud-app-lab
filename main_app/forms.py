# main_app/forms.py
from django.contrib.auth.models import User 
from django import forms
from .models import Car, Maintenance, Part





class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['name', 'model', 'year']  # Adjust fields as per your Car model

class PartForm(forms.ModelForm):
    class Meta:
        model = Part
        fields = ['name', 'description', 'price', 'car']  # Ensure these fields exist in the model


class MaintenanceForm(forms.ModelForm):
    class Meta:
        model = Maintenance
        fields = ['date', 'description']  # Ensure these fields exist in the model

class SignupForm(forms.ModelForm):  # Corrected class name to 'SignupForm'
    class Meta:
        model = User
        fields = ['username', 'email', 'password']  # Ensure these fields exist in the model
        widgets = {
            'password': forms.PasswordInput(),
        }