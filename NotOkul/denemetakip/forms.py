from django import forms
from .models import DenemeTakip, DenemeTakipAYT


class DenemeTakipForm(forms.ModelForm):
    class Meta:
        model = DenemeTakip

        fields = [
            'title',
            'netSayisi',
            'publisher',
            'created_date',
            #    'created_date',

        ]
        """
        widgets = {
          'created_date': forms.DateInput(attrs={'class': 'form-control created_date'}),
          'created_date': forms.DateInput(attrs={'placeholder': 'Lütfen gg/aa/yyyy formatında deneme tarihini girin. '}),

        }
         """


class DenemeTakipAYTForm(forms.ModelForm):
    class Meta:
        model = DenemeTakipAYT
        fields = [
            'title',
            'publisher',
            'matNet',
            'fizikNet',
            'kimyaNet',
            'biyoNet',
        ]
