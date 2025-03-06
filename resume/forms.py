# forms.py
from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'phone', 'message']
        


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'phone', 'message']
        widgets = {
            'message': forms.Textarea(attrs={
                'rows': 3,  # Reduce the number of rows
                'cols': 50,  # Optionally set the width
                'placeholder': 'Enter your message here...',  # Add a placeholder
                'class': 'form-control',  # Add Bootstrap styling if needed
            }),
        }

