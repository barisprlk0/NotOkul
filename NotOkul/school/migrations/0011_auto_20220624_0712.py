# Generated by Django 3.2 on 2022-06-24 04:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0010_auto_20220624_0712'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schoolnote',
            name='lesson',
            field=models.CharField(choices=[('AYT Fizik', 'AYT Fizik'), ('TYT Matematik', 'TYT Matematik'), ('TYT Sosyal Bilimler', 'TYT Sosyal Bilimler'), ('AYT Kimya', 'AYT Kimya'), ('TYT Türkçe', 'TYT Türkçe'), ('AYT Matematik', 'AYT Matematik'), ('AYT Biyoloji', 'AYT Biyoloji'), ('TYT Fen Bilimleri', 'TYT Fen Bilimleri')], max_length=30, verbose_name='Ders Adı'),
        ),
        migrations.AlterField(
            model_name='testsihirbazi',
            name='lesson',
            field=models.CharField(choices=[('AYT Fizik', 'AYT Fizik'), ('TYT Matematik', 'TYT Matematik'), ('AYT Kimya', 'AYT Kimya'), ('TYT Türkçe', 'TYT Türkçe'), ('AYT Matematik', 'AYT Matematik'), ('AYT Biyoloji', 'AYT Biyoloji')], max_length=50, verbose_name='Ders Adı'),
        ),
        migrations.AlterField(
            model_name='testsihirbazi',
            name='net_araligi',
            field=models.CharField(choices=[('0-10', '0-10'), ('30-40', '30-40'), ('10-20', '10-20'), ('25-30', '25-30'), ('20-25', '20-25')], max_length=50, verbose_name='Net Aralığınız'),
        ),
    ]
