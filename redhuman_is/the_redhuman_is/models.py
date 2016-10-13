# -*- coding: utf-8 -*-
""" id = models.AutoField(primary_key=True) нужно ли? см.http://djbook.ru/rel1.9/topics/db/models.html
"""
from __future__ import unicode_literals

import datetime
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils import timezone
# Create your models here.
class Worker(models.Model):
    input_date = models.DateTimeField(blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    patronymic = models.CharField(max_length=100, blank=True, null=True)
    passport_number = models.CharField(max_length=9, blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    mig_series = models.IntegerField(blank=True, null=True)
    mig_number = models.IntegerField(blank=True, null=True)
    m_date_of_issue = models.DateField(blank=True, null=True)
    m_date_of_exp = models.DateField(blank=True, null=True)

    class Meta:
        pass#Поправить потом

    def __str__(self):
        return self.last_name


    def save_worker(self):
        self.input_date = timezone.now()
        self.save()

class WorkerPassport(models.Model):
    workers_id = models.ForeignKey(Worker, on_delete=models.CASCADE)
    passport_type = models.CharField(max_length=15, blank=True, null=True)
    another_passport_number = models.CharField(max_length=9, blank=True, null=True)
    date_of_issue = models.DateField(blank=True, null=True)
    date_of_exp = models.DateField(blank=True, null=True)
    issued_by = models.CharField(max_length=100, blank=True, null=True)

class WorkerRegistration(models.Model):
    workers_id = models.ForeignKey(Worker, on_delete=models.CASCADE)
    city = models.CharField(max_length=100, blank=True, null=True)
    street = models.CharField(max_length=100, blank=True, null=True)
    house_number = models.CharField(max_length=100, blank=True, null=True)
    building_number = models.CharField(max_length=100, blank=True, null=True)
    appt_number = models.CharField(max_length=100, blank=True, null=True)

class TelNumber(models.Model):
    workers_id = models.ForeignKey(Worker, on_delete=models.CASCADE)
    tel_number = models.IntegerField(default=89, blank=True, null=True)
    votes = models.IntegerField(default=0, blank=True, null=True)

class Customer(models.Model):
    cust_name = models.CharField(max_length=100, blank=True, null=True)

class CustomerLocation(models.Model):
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    location_name = models.CharField(max_length=100, blank=True, null=True)
    location_adress = models.CharField(max_length=100, blank=True, null=True)
    location_how_to_get = models.CharField(max_length=100, blank=True, null=True)

class CustomerRepr(models.Model):
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    repr_last_name = models.CharField(max_length=100, blank=True, null=True)
    repr_name = models.CharField(max_length=100, blank=True, null=True)
    repr_patronymic = models.CharField(max_length=100, blank=True, null=True)
    #tel_number = """Че сюда писать надо разобрацца"""

class Timesheet(models.Model):
    cust_name = models.CharField(max_length=100, blank=True, null=True)

class WorkerTurnout(models.Model):
    cust_name = models.CharField(max_length=100, blank=True, null=True)
