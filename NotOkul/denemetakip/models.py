from django.db import models

# Create your models here.


class DenemeTakip(models.Model):

    title = models.CharField(verbose_name="Deneme Adı", max_length=255)
    netSayisi = models.IntegerField(verbose_name="Toplam Net")
    publisher = models.CharField(verbose_name="Yayınevi", max_length=255)
    user = models.ForeignKey('auth.User', verbose_name="Öğrenci",
                             on_delete=models.CASCADE, related_name='denemetakip')
    created_date = models.DateTimeField(
        verbose_name="Tarih", editable=True)

    def __str__(self):
        return "{}-{}-{}-{}".format(self.title, self.netSayisi, self.publisher, self.created_date)


class DenemeTakipAYT(models.Model):
    user = models.ForeignKey('auth.User', verbose_name="Öğrenci",
                             on_delete=models.CASCADE, related_name='denemetakipayt')
    title = models.CharField(verbose_name="Deneme Adı", max_length=255)
    matNet = models.IntegerField(verbose_name="Matematik Neti")
    fizikNet = models.IntegerField(verbose_name="Fizik Neti")
    kimyaNet = models.IntegerField(verbose_name="Kimya Neti")
    biyoNet = models.IntegerField(verbose_name="Biyoloji Neti")
    netSayisi = models.IntegerField(verbose_name="ToplamNet")

    publisher = models.CharField(verbose_name="Yayınevi", max_length=255)

    created_date = models.DateField(
        auto_now_add=True, verbose_name="Tarih", editable=True)

    def __str__(self):
        return "{}-{}-{}-{}".format(self.title, self.matNet, self.fizikNet, self.kimyaNet, self.biyoNet, self.publisher, self.created_date)

    class Meta:
        ordering = ['-created_date']
