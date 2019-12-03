from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import datetime


class Student(models.Model):
    name = models.CharField(default = 'John', max_length = 255, verbose_name = 'Имя студента')
    surname = models.CharField(default = 'Doe', max_length = 255, verbose_name = 'Фамилия студента')
    group = models.IntegerField(default = 0, verbose_name = 'Номер группы')
    faculty = models.CharField(default = 'None', max_length = 255, verbose_name = 'Факультет')
    specialty = models.CharField(default = 'None', max_length = 255, verbose_name = 'Специальность')
    entry_date = models.DateField(default = datetime.today, verbose_name = 'Дата поступления')


class Message(models.Model):
    chat = models.ForeignKey(Student, verbose_name='Чат под студентом', on_delete=models.CASCADE)
    author = models.ForeignKey(User, verbose_name='Кто оставил комментарий', on_delete=models.CASCADE)
    message = models.TextField('Сообщение')
    pub_date = models.DateTimeField('Дата сообщения', default=timezone.now)


class Mark(models.Model):
    student = models.ForeignKey(Student, verbose_name = 'Студент', on_delete = models.CASCADE, default = None)
    author = models.ForeignKey(User, verbose_name='Кто поставил оценку', on_delete=models.CASCADE)
    mark = models.IntegerField(verbose_name='Оценка')
    pub_date = models.DateTimeField('Дата оценки', default=timezone.now)
