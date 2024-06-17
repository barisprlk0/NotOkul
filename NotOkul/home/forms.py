from django import forms
from home.models import ContactModel

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactModel
        fields = [
        'subject',
        'content',
        

        ]
