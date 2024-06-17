from django.db import models

# Create your models here.

class TodoModel(models.Model):
    title = models.CharField(verbose_name="Başlık" , blank=True , null=True , max_length=255)
    question = models.IntegerField(verbose_name="Soru Hedefi" , blank=True , null=True)
    time = models.IntegerField(verbose_name="Vakit Hedefi" , blank=True , null=True)
    user = models.ForeignKey('auth.User' ,verbose_name="Kullanıcı" , on_delete=models.CASCADE , related_name='Todo')
    created_date = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_date']
