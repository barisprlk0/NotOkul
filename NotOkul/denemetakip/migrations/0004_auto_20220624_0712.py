# Generated by Django 3.2 on 2022-06-24 04:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('denemetakip', '0003_auto_20210820_2330'),
    ]

    operations = [
        migrations.AddField(
            model_name='denemetakip',
            name='toplamNet',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='denemetakip',
            name='type',
            field=models.CharField(choices=[('TYT', 'TYT'), ('AYT', 'AYT')], max_length=255, verbose_name='Deneme Tipi'),
        ),
    ]