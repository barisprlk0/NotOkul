# Generated by Django 3.2 on 2022-11-15 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0021_auto_20221026_1224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schoolnote',
            name='lesson',
            field=models.CharField(choices=[('AYT Kimya', 'AYT Kimya'), ('TYT Fizik', 'TYT Fizik'), ('TYT Sosyal Bilimler', 'TYT Sosyal Bilimler'), ('AYT Fizik', 'AYT Fizik'), ('TYT Matematik', 'TYT Matematik'), ('TYT Biyoloji', 'TYT Biyoloji'), ('TYT Kimya', 'TYT Kimya'), ('AYT Matematik', 'AYT Matematik'), ('AYT Biyoloji', 'AYT Biyoloji'), ('TYT Türkçe', 'TYT Türkçe')], max_length=30, verbose_name='Ders Adı'),
        ),
        migrations.AlterField(
            model_name='testsihirbazi',
            name='lesson',
            field=models.CharField(choices=[('AYT Kimya', 'AYT Kimya'), ('AYT Fizik', 'AYT Fizik'), ('TYT Matematik', 'TYT Matematik'), ('AYT Matematik', 'AYT Matematik'), ('AYT Biyoloji', 'AYT Biyoloji'), ('TYT Türkçe', 'TYT Türkçe')], max_length=50, verbose_name='Ders Adı'),
        ),
        migrations.AlterField(
            model_name='testsihirbazi',
            name='net_araligi',
            field=models.CharField(choices=[('30-40', '30-40'), ('10-20', '10-20'), ('0-10', '0-10'), ('25-30', '25-30'), ('20-25', '20-25')], max_length=50, verbose_name='Net Aralığınız'),
        ),
    ]
