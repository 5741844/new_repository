# -*- coding: utf-8 -*-
""" id = models.AutoField(primary_key=True) нужно ли? см.http://djbook.ru/rel1.9/topics/db/models.html
"""
from __future__ import unicode_literals

import datetime
from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.utils.encoding import python_2_unicode_compatible
from django.utils import timezone
# Create your models here.
class Worker(models.Model):
    input_date = models.DateTimeField("Дата внесения", blank=True, null=True)
    last_name = models.CharField("Фамилия", max_length=100, blank=True, null=True)
    name = models.CharField("Имя", max_length=100, blank=True, null=True)
    patronymic = models.CharField("Отчество", max_length=100, blank=True, null=True)
    passport_number = models.CharField("Номер паспорта", max_length=9, blank=True, null=True)
    birth_date = models.DateField("Дата рождения", blank=True, null=True, help_text="Формат ввода: <em>дд.мм.гггг</em>")
    mig_series = models.IntegerField("Миграционная карта, серия", blank=True, null=True)
    mig_number = models.IntegerField("Миграционная карта, номер", blank=True, null=True)
    m_date_of_issue = models.DateField("Миграционная карта, дата выдачи", blank=True, null=True)
    m_date_of_exp = models.DateField("Миграционная карта, дата окончания", blank=True, null=True)
    #tel_number = generic.GenericRelation(TelNumber, content_type_field=’entity_type’, object_id_field=’entity_id’)

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

    def __unicode__(self):
    # You can access ForeignKey properties through the field name!
        return self.workerpassport.workers_id

class WorkerRegistration(models.Model):
    workers_id = models.ForeignKey(Worker, on_delete=models.CASCADE)
    city = models.CharField(max_length=100, blank=True, null=True)
    street = models.CharField(max_length=100, blank=True, null=True)
    house_number = models.CharField(max_length=100, blank=True, null=True)
    building_number = models.CharField(max_length=100, blank=True, null=True)
    appt_number = models.CharField(max_length=100, blank=True, null=True)

    def __unicode__(self):
        return self.workerregistration.workers_id

#class TelNumber(models.Model):
    #entity_type = models.ForeignKey(ContentType, blank=True, null=True, verbose_name="Type")
    #entity_id = models.PositiveIntegerField(blank=True, null=True, editable=True, verbose_name=u"Link")
    #item = generic.GenericForeignKey('entity_type', 'entity_id')
    #tel_number = models.IntegerField(default=89, blank=True, null=True)

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
    #tel_number = generic.GenericRelation(TelNumber, content_type_field=’entity_type’, object_id_field=’entity_id’)

class Timesheet(models.Model):
    sheet_date = models.DateField(blank=True, null=True)
    sheet_turn = models.CharField(max_length=100, blank=True, null=True)
    cust_location = models.ForeignKey(CustomerLocation, on_delete=models.CASCADE)#Автоматом подтягивать и имя заказчика
    foreman = models.ForeignKey(Worker, on_delete=models.CASCADE)
    turnouts_number = models.IntegerField(blank=True, null=True)

class WorkerTurnout(models.Model):
    timesheet = models.ForeignKey(Timesheet, on_delete=models.CASCADE)
    worker_id = models.ForeignKey(Worker, on_delete=models.CASCADE)
    worker_function = models.CharField(max_length=100, blank=True, null=True)
    hours_worked = models.DecimalField(max_digits=3, decimal_places=1)
