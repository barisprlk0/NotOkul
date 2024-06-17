# Generated by Django 3.2 on 2021-08-10 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0003_auto_20210809_1644'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schoolnote',
            name='lesson',
            field=models.CharField(choices=[('TYT Matematik', 'TYT Matematik'), ('TYT Sosyal Bilimler', 'TYT Sosyal Bilimler'), ('AYT Fizik', 'AYT Fizik'), ('AYT Kimya', 'AYT Kimya'), ('TYT Türkçe', 'TYT Türkçe'), ('TYT Fen Bilimleri', 'TYT Fen Bilimleri'), ('AYT Biyoloji', 'AYT Biyoloji'), ('AYT Matematik', 'AYT Matematik')], max_length=30, verbose_name='Ders Adı'),
        ),
        migrations.AlterField(
            model_name='testsihirbazi',
            name='lesson',
            field=models.CharField(choices=[('TYT Matematik', 'TYT Matematik'), ('AYT Fizik', 'AYT Fizik'), ('AYT Kimya', 'AYT Kimya'), ('TYT Türkçe', 'TYT Türkçe'), ('AYT Biyoloji', 'AYT Biyoloji'), ('AYT Matematik', 'AYT Matematik')], max_length=50, verbose_name='Ders Adı'),
        ),
        migrations.AlterField(
            model_name='testsihirbazi',
            name='net_araligi',
            field=models.CharField(choices=[('0-10', '0-10'), ('20-25', '20-25'), ('25-30', '25-30'), ('10-20', '10-20'), ('30-40', '30-40')], max_length=50, verbose_name='Net Aralığınız'),
        ),
    ]