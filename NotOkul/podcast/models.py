from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Podcast(models.Model):
    lesson_choices = {
    #tyt
    ('TYT Türkçe','TYT Türkçe'),
    ('TYT Matematik' , 'TYT Matematik'),
    }
    lesson = models.CharField(verbose_name="Ders" , max_length=50 , choices=lesson_choices)

    subject_choices = {
    ('Sözcükte Anlam','Sözcükte Anlam'),
    ('Cümlede Anlam','Cümlede Anlam'),
    ('Paragrafta Anlam','Paragrafta Anlam')
    }
    subject = models.CharField(verbose_name="Ders", max_length=255 , choices=subject_choices)

    author = models.ForeignKey('auth.user' , verbose_name='Gönderen',on_delete=models.CASCADE,related_name="podcast")

    sound = models.FileField(verbose_name="Podcast Kaydı" )

    publishing_date = models.DateTimeField(verbose_name="Tarih",auto_now_add=True)

    class Meta:
        ordering = ['-publishing_date']
