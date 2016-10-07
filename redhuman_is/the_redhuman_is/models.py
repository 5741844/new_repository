# -*- coding: utf-8 -*-
""" id = models.AutoField(primary_key=True) нужно ли? см.http://djbook.ru/rel1.9/topics/db/models.html
строка 17 в  паспорте #int_or_foreign = #сюда надо вставить условие, если переменная х == внутренний, то значение "внутренний", иначе "заграничный"" """

from __future__ import unicode_literals
from django.db import models

# Create your models here.
class Worker(models.Model):
    last_name = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    patronymic = models.CharField(max_length=100)
    passport_number = models.CharField(max_length=9)
    birth_date = models.DateField()

class WorkerPassport(models.Model):
    worker_id = models.ForeignKey(Worker, on_delete=models.CASCADE)
    another_passport_number = models.CharField(max_length=9)
    date_of_issue = models.DateField()
    date_of_exp = models.DateField()
    issued_by = models.CharField(max_length=100)

class WorkerRegistration(models.Model):
    worker_id = models.ForeignKey(Worker, on_delete=models.CASCADE)
    city = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    house_number = models.CharField(max_length=100)
    building_number = models.CharField(max_length=100)
    appt_number = models.CharField(max_length=100)

class WorkerMigrationCard(models.Model):
    worker_id = models.ForeignKey(Worker, on_delete=models.CASCADE)
    series = models.IntegerField()
    number = models.IntegerField()
