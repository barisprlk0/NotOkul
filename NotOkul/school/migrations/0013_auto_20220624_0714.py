# Generated by Django 3.2 on 2022-06-24 04:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0012_auto_20220624_0713'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schoolnote',
            name='lesson',
            field=models.CharField(choices=[('TYT Sosyal Bilimler', 'TYT Sosyal Bilimler'), ('AYT Biyoloji', 'AYT Biyoloji'), ('TYT Matematik', 'TYT Matematik'), ('AYT Matematik', 'AYT Matematik'), ('AYT Kimya', 'AYT Kimya'), ('AYT Fizik', 'AYT Fizik'), ('TYT Türkçe', 'TYT Türkçe'), ('TYT Fen Bilimleri', 'TYT Fen Bilimleri')], max_length=30, verbose_name='Ders Adı'),
        ),
        migrations.AlterField(
            model_name='testsihirbazi',
            name='lesson',
            field=models.CharField(choices=[('AYT Biyoloji', 'AYT Biyoloji'), ('TYT Matematik', 'TYT Matematik'), ('AYT Matematik', 'AYT Matematik'), ('AYT Kimya', 'AYT Kimya'), ('AYT Fizik', 'AYT Fizik'), ('TYT Türkçe', 'TYT Türkçe')], max_length=50, verbose_name='Ders Adı'),
        ),
        migrations.AlterField(
            model_name='testsihirbazi',
            name='net_araligi',
            field=models.CharField(choices=[('25-30', '25-30'), ('30-40', '30-40'), ('20-25', '20-25'), ('0-10', '0-10'), ('10-20', '10-20')], max_length=50, verbose_name='Net Aralığınız'),
        ),
    ]
