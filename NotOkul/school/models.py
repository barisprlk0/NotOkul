from django.db import models

# Create your models here.


class SchoolNote(models.Model):
    lesson_choices = {
        #tyt
        ('TYT Türkçe', 'TYT Türkçe'),
        ('TYT Matematik', 'TYT Matematik'),
        ('TYT Fizik', 'TYT Fizik'),
        ('TYT Kimya', 'TYT Kimya'),
        ('TYT Biyoloji', 'TYT Biyoloji'),
        ('TYT Sosyal Bilimler', 'TYT Sosyal Bilimler'),
        #ayt sayısal
        ('AYT Matematik', 'AYT Matematik'),
        ('AYT Fizik', 'AYT Fizik'),
        ('AYT Kimya', 'AYT Kimya'),
        ('AYT Biyoloji', 'AYT Biyoloji'),


    }
    lesson = models.CharField(verbose_name="Ders Adı",
                              max_length=30, choices=lesson_choices)
    subject = models.CharField(verbose_name="Konu Adı", max_length=150)
    time = models.IntegerField(
        verbose_name="Çalışma Süresi (Dakika)")
    question = models.IntegerField(verbose_name="Soru Sayısı")
    note = models.TextField(verbose_name="Notlar", null=True, blank=True)
    publishing_date = models.DateTimeField(
        verbose_name="Tarih", auto_now_add=True)
    author = models.ForeignKey(
        'auth.User', verbose_name="Öğrenci", on_delete=models.CASCADE, related_name='NetOkul')

    class Meta:
        ordering = ["-publishing_date"]


class TestSihirbazi(models.Model):
    lesson_choices = {
        #tyt
        ('TYT Türkçe', 'TYT Türkçe'),
        ('TYT Matematik', 'TYT Matematik'),


        #ayt sayısal
        ('AYT Matematik', 'AYT Matematik'),
        ('AYT Fizik', 'AYT Fizik'),
        ('AYT Kimya', 'AYT Kimya'),
        ('AYT Biyoloji', 'AYT Biyoloji'),


    }

    lesson = models.CharField(verbose_name="Ders Adı",
                              max_length=50, choices=lesson_choices)

    net_choices = {
        ('0-10', '0-10'),
        ('10-20', '10-20'),
        ('20-25', '20-25'),
        ('25-30', '25-30'),
        ('30-40', '30-40'),
    }
    net_araligi = models.CharField(
        verbose_name="Net Aralığınız", max_length=50, choices=net_choices)
