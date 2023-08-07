from django.forms import ModelForm
# from .models import Register
from django import forms
# class RegisterForm(ModelForm):
#     class Meta:
#         model = Register
#         fields = '__all__'
#
#         widgets = {
#             'job': forms.Select(attrs={'class': 'form-control'}),
#             'education': forms.Select(attrs={'class': 'form-control'}),
#             'experience': forms.Select(attrs={'class': 'form-control'}),
#         }

from django import forms
from .models import MyUser

class RegistrationForm(forms.ModelForm):

    class Meta:
        model = MyUser
        fields = ['email', 'mobile', 'first_name', 'last_name', 'job', 'education', 'experience']
        widgets = {
                    'job': forms.Select(attrs={'class': 'form-control'}),
                    'education': forms.Select(attrs={'class': 'form-control'}),
                    'experience': forms.Select(attrs={'class': 'form-control'}),
                }