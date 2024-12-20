# Generated by Django 3.2 on 2022-09-18 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0016_auto_20220624_0743'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schoolnote',
            name='lesson',
            field=models.CharField(choices=[('TYT Sosyal Bilimler', 'TYT Sosyal Bilimler'), ('TYT Türkçe', 'TYT Türkçe'), ('TYT Biyoloji', 'TYT Biyoloji'), ('TYT Matematik', 'TYT Matematik'), ('AYT Biyoloji', 'AYT Biyoloji'), ('TYT Kimya', 'TYT Kimya'), ('TYT Fizik', 'TYT Fizik'), ('AYT Kimya', 'AYT Kimya'), ('AYT Matematik', 'AYT Matematik'), ('AYT Fizik', 'AYT Fizik')], max_length=30, verbose_name='Ders Adı'),
        ),
        migrations.AlterField(
            model_name='testsihirbazi',
            name='lesson',
            field=models.CharField(choices=[('TYT Türkçe', 'TYT Türkçe'), ('TYT Matematik', 'TYT Matematik'), ('AYT Biyoloji', 'AYT Biyoloji'), ('AYT Kimya', 'AYT Kimya'), ('AYT Matematik', 'AYT Matematik'), ('AYT Fizik', 'AYT Fizik')], max_length=50, verbose_name='Ders Adı'),
        ),
        migrations.AlterField(
            model_name='testsihirbazi',
            name='net_araligi',
            field=models.CharField(choices=[('0-10', '0-10'), ('25-30', '25-30'), ('20-25', '20-25'), ('30-40', '30-40'), ('10-20', '10-20')], max_length=50, verbose_name='Net Aralığınız'),
        ),
    ]
