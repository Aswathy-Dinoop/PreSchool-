from django import forms
from django.forms import ModelForm, RadioSelect, TextInput, FileInput
from django.core.exceptions import ValidationError

from preschoolapp.models import ChildDetails

class ChildForm(ModelForm):
    class Meta:
        model = ChildDetails
        fields = ['name','age','birthcertificate','image','gender']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Add Name', 'pattern': '[A-Za-z]+','title': 'Please enter letters only (no white space)'}),
            'age': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Add Age', 'min': 2, 'max': 6, 'title': 'Please enter a number between 2 and 6'}),
            'birthcertificate': forms.ClearableFileInput(attrs={'class': 'form-control', 'placeholder': 'Add birthcertificate', 'accept': 'application/pdf'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control', 'placeholder': 'Add image', 'accept': 'image/*'}),
            'gender': RadioSelect(choices=ChildDetails.GENDER_CHOICES),

    
        }
    # def clean_age(self):
    #     age = self.cleaned_data.get('age')
    #     if age is not None and (age < 2 or age > 6):
    #         raise forms.ValidationError("Age must be between 2 and 6 years.")
    #     return age