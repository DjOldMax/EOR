# Generated by Django 4.0.5 on 2022-06-27 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BOOKS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Название книги')),
                ('discription', models.CharField(max_length=20, verbose_name='Описание книги')),
                ('image', models.CharField(max_length=20, verbose_name='Раположение обложки')),
                ('way', models.CharField(max_length=20, verbose_name='Раположение файла')),
            ],
            options={
                'verbose_name': 'Литература',
                'verbose_name_plural': 'Литература',
            },
        ),
    ]