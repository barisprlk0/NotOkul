# Generated by Django 3.2 on 2022-06-24 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('podcast', '0012_auto_20220624_0727'),
    ]

    operations = [
        migrations.AlterField(
            model_name='podcast',
            name='subject',
            field=models.CharField(choices=[('Cümlede Anlam', 'Cümlede Anlam'), ('Paragrafta Anlam', 'Paragrafta Anlam'), ('Sözcükte Anlam', 'Sözcükte Anlam')], max_length=255, verbose_name='Ders'),
        ),
    ]
