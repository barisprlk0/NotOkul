from django.forms import models
from .models import SchoolNote
from .models import TestSihirbazi

class SchoolNoteForm(models.ModelForm):
    class Meta:
        model = SchoolNote
        fields = [
        'lesson',
        'subject',
        'time',
        'question',
        'note',

        ]

class TestSihirbaziForm(models.ModelForm):
    class Meta:
        model = TestSihirbazi
        fields = [
        'lesson',
        'net_araligi',

        ]
