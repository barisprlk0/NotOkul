from django.db import models

# Create your models here.

class ContactModel(models.Model):
    subject = models.CharField(verbose_name = "Başlık" , max_length=500)
    content = models.TextField(verbose_name = "Konu")
