from django.forms import ModelForm
from .models import Register
from django import forms
class RegisterForm(ModelForm):
    class Meta:
        model = Register
        fields = '__all__'

        widgets = {
            'job': forms.Select(attrs={'class': 'form-control'}),
            'education': forms.Select(attrs={'class': 'form-control'}),
            'experience': forms.Select(attrs={'class': 'form-control'}),
        }