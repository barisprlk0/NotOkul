# Generated by Django 3.2 on 2022-06-24 04:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0013_auto_20220624_0714'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schoolnote',
            name='lesson',
            field=models.CharField(choices=[('AYT Matematik', 'AYT Matematik'), ('TYT Türkçe', 'TYT Türkçe'), ('TYT Sosyal Bilimler', 'TYT Sosyal Bilimler'), ('AYT Kimya', 'AYT Kimya'), ('TYT Matematik', 'TYT Matematik'), ('AYT Biyoloji', 'AYT Biyoloji'), ('AYT Fizik', 'AYT Fizik'), ('TYT Fen Bilimleri', 'TYT Fen Bilimleri')], max_length=30, verbose_name='Ders Adı'),
        ),
        migrations.AlterField(
            model_name='testsihirbazi',
            name='lesson',
            field=models.CharField(choices=[('AYT Matematik', 'AYT Matematik'), ('TYT Türkçe', 'TYT Türkçe'), ('TYT Matematik', 'TYT Matematik'), ('AYT Biyoloji', 'AYT Biyoloji'), ('AYT Fizik', 'AYT Fizik'), ('AYT Kimya', 'AYT Kimya')], max_length=50, verbose_name='Ders Adı'),
        ),
        migrations.AlterField(
            model_name='testsihirbazi',
            name='net_araligi',
            field=models.CharField(choices=[('10-20', '10-20'), ('0-10', '0-10'), ('30-40', '30-40'), ('25-30', '25-30'), ('20-25', '20-25')], max_length=50, verbose_name='Net Aralığınız'),
        ),
    ]
