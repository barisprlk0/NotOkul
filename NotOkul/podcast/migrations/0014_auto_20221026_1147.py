# Generated by Django 3.2 on 2022-10-26 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('podcast', '0013_alter_podcast_subject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='podcast',
            name='lesson',
            field=models.CharField(choices=[('TYT Matematik', 'TYT Matematik'), ('TYT Türkçe', 'TYT Türkçe')], max_length=50, verbose_name='Ders'),
        ),
        migrations.AlterField(
            model_name='podcast',
            name='subject',
            field=models.CharField(choices=[('Sözcükte Anlam', 'Sözcükte Anlam'), ('Cümlede Anlam', 'Cümlede Anlam'), ('Paragrafta Anlam', 'Paragrafta Anlam')], max_length=255, verbose_name='Ders'),
        ),
    ]
