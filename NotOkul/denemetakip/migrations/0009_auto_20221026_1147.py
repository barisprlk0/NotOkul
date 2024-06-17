# Generated by Django 3.2 on 2022-10-26 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('denemetakip', '0008_auto_20220624_0727'),
    ]

    operations = [
        migrations.CreateModel(
            name='DenemeTakipAYT',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Deneme Adı')),
                ('matNet', models.IntegerField(verbose_name='Matematik Neti')),
                ('fizikNet', models.IntegerField(verbose_name='Fizik Neti')),
                ('kimyaNet', models.IntegerField(verbose_name='Kimya Neti')),
                ('biyoNet', models.IntegerField(verbose_name='Biyoloji Neti')),
                ('publisher', models.CharField(max_length=255, verbose_name='Yayınevi')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Tarih')),
            ],
        ),
        migrations.AlterField(
            model_name='denemetakip',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Tarih'),
        ),
    ]
