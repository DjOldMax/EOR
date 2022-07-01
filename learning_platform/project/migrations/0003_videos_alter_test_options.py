# Generated by Django 4.0.5 on 2022-06-30 18:17

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0002_test'),
    ]

    operations = [
        migrations.CreateModel(
            name='VIDEOS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Заголовок')),
                ('description', models.TextField(verbose_name='Описание')),
                ('image', models.ImageField(upload_to='image/', verbose_name='Заставка')),
                ('file', models.FileField(upload_to='video/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['mp4'])], verbose_name='Вопрос')),
            ],
        ),
        migrations.AlterModelOptions(
            name='test',
            options={'verbose_name': 'Вопросы теста', 'verbose_name_plural': 'Вопросы теста'},
        ),
    ]