# Generated by Django 3.2 on 2021-08-20 20:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_todomodel_status'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='todomodel',
            options={'ordering': ['-created_date']},
        ),
    ]
