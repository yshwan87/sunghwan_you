from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"

def clean_name(self):
        name = self.cleaned_data['name']
        if Contact.objects.filter(name=name).exists():
            raise forms.ValidationError('Name already exists. Please choose a different name.')
        return name

def clean_email(self):
    email = self.cleaned_data['email']
    # You can add more sophisticated email validation if needed
    if not email.endswith('@example.com'):  # Replace with your desired validation logic
        raise forms.ValidationError('Invalid email address.')
    return email