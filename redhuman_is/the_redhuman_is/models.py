# -*- coding: utf-8 -*-
""" id = models.AutoField(primary_key=True) нужно ли? см.http://djbook.ru/rel1.9/topics/db/models.html
строка 17 в  паспорте #int_or_foreign = #сюда надо вставить условие, если переменная х == внутренний, то значение "внутренний", иначе "заграничный"" """

from __future__ import unicode_literals

import datetime
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils import timezone

# Create your models here.
class Worker(models.Model):
    input_date = models.DateTimeField('date published')
    last_name = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    patronymic = models.CharField(max_length=100)
    passport_number = models.CharField(max_length=9)
    birth_date = models.DateField()
    mig_series = models.IntegerField()
    mig_number = models.IntegerField()
    m_date_of_issue = models.DateField()
    m_date_of_exp = models.DateField()

    def __str__(self):
        return self.name

    def __str__(self):
        return self.last_name

    def was_born_recently(self):
        return self.birth_date >= (timezone.now() - datetime.timedelta(days=1))

class WorkerPassport(models.Model):
    workers_id = models.ForeignKey(Worker, on_delete=models.CASCADE)
    another_passport_number = models.CharField(max_length=9)
    date_of_issue = models.DateField()
    date_of_exp = models.DateField()
    issued_by = models.CharField(max_length=100)

class WorkerRegistration(models.Model):
    workers_id = models.ForeignKey(Worker, on_delete=models.CASCADE)
    city = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    house_number = models.CharField(max_length=100)
    building_number = models.CharField(max_length=100)
    appt_number = models.CharField(max_length=100)

class TelNumber(models.Model):
    workers_id = models.ForeignKey(Worker, on_delete=models.CASCADE)
    tel_number = models.IntegerField(default=89)
