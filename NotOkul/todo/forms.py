from django import forms
from .models import TodoModel

class TodoForm(forms.ModelForm):
    class Meta:
        model = TodoModel
        fields = ['title','question','time' ]

        widgets = {
          'title': forms.TextInput(attrs={'class': 'form-control titleTD'}),
          'question': forms.TextInput(attrs={'class': 'form-control questionTD'}),
          'time': forms.TextInput(attrs={'class': 'form-control timeTD'}),
        }
