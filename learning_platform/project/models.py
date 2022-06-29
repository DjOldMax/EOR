from django.db import models
from django.urls import reverse
# Create your models here.
class BOOKS(models.Model):

    name =  models.CharField(max_length=20,verbose_name='Название книги')
    discription =  models.CharField(max_length=20,verbose_name='Описание книги')
    image =  models.CharField(max_length=20,verbose_name='Раположение обложки')
    way =  models.CharField(max_length=20,verbose_name='Раположение файла')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('book',kwargs={'book_id': self.pk})
    class Meta:
        verbose_name = 'Литература'
        verbose_name_plural = 'Литература'

class TEST(models.Model):

    question =  models.CharField(max_length=20,verbose_name='Вопрос')
    modul = models.CharField(max_length=20,verbose_name='Раздел')
    answer0 =  models.CharField(max_length=20,verbose_name='Верный ответ')
    answer1 =  models.CharField(max_length=20,verbose_name='Прочий ответ')
    answer2 =  models.CharField(max_length=20,verbose_name='Прочий ответ')
    answer3 =  models.CharField(max_length=20,verbose_name='Просий ответ')

    def __str__(self):
        return self.question

    class Meta:
        verbose_name = 'Вопросы теста'
        verbose_name_plural = 'Вопросы теста'