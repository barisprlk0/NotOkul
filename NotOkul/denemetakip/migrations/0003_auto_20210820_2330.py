# Generated by Django 3.2 on 2021-08-20 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('denemetakip', '0002_auto_20210820_2327'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='denemetakip',
            name='note',
        ),
        migrations.AlterField(
            model_name='denemetakip',
            name='type',
            field=models.CharField(choices=[('AYT', 'AYT'), ('TYT', 'TYT')], max_length=255, verbose_name='Deneme Tipi'),
        ),
    ]