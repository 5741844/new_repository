# -*- coding: utf-8 -*-
""" id = models.AutoField(primary_key=True) нужно ли? см.http://djbook.ru/rel1.9/topics/db/models.html
"""
from __future__ import unicode_literals

import datetime
from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.utils.encoding import python_2_unicode_compatible
from django.utils.encoding import smart_unicode
from django.utils import timezone
# Create your models here.
"""def update_filename(instance, filename):
    path = "workers"
    format = instance.last_name + instance.name + instance.patronymic
    return os.path.join(path, format)"""

def upload_location(instance, filename):
    return "workers/%s %s %s/%s" % (instance.last_name, instance.name, instance.patronymic, filename)

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
    image1 = models.ImageField(
        upload_to=upload_location,
        null=True,
        blank=True,
        width_field='width_field',
        height_field='height_field')
    image2 = models.ImageField(
        upload_to=upload_location,
        null=True,
        blank=True,
        width_field='width_field',
        height_field='height_field')
    image3 = models.ImageField(
        upload_to=upload_location,
        null=True,
        blank=True,
        width_field='width_field',
        height_field='height_field')
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)


    class Meta:
        pass#Поправить потом

    def __unicode__(self):
        return smart_unicode(self.last_name)

    #def __unicode__(self):
        #return u"%s" % self.your_field


    def save_worker(self):
        self.input_date = timezone.now()
        self.save()

class WorkerPassport(models.Model):
    workers_id = models.ForeignKey(Worker, on_delete=models.CASCADE)
    passport_type = models.CharField("Тип паспорта", max_length=15, blank=True, null=True)
    another_passport_number = models.CharField("Номер паспорта", max_length=9, blank=True, null=True)
    date_of_issue = models.DateField("Дата выдачи", blank=True, null=True)
    date_of_exp = models.DateField("Дата окончания", blank=True, null=True)
    issued_by = models.CharField("Кем выдан", max_length=100, blank=True, null=True)

    def __unicode__(self):
    # You can access ForeignKey properties through the field name!
        return self.workerpassport.workers_id

class WorkerRegistration(models.Model):
    workers_id = models.ForeignKey(Worker, on_delete=models.CASCADE)
    city = models.CharField("Город", max_length=100, blank=True, null=True)
    street = models.CharField("Улица", max_length=100, blank=True, null=True)
    house_number = models.CharField("Дом", max_length=100, blank=True, null=True)
    building_number = models.CharField("Строение", max_length=100, blank=True, null=True)
    appt_number = models.CharField("Квартира", max_length=100, blank=True, null=True)

    def __unicode__(self):
        return self.workerregistration.workers_id

#class TelNumber(models.Model):
    #entity_type = models.ForeignKey(ContentType, blank=True, null=True, verbose_name="Type")
    #entity_id = models.PositiveIntegerField(blank=True, null=True, editable=True, verbose_name=u"Link")
    #item = generic.GenericForeignKey('entity_type', 'entity_id')
    #tel_number = models.IntegerField(default=89, blank=True, null=True)

class Customer(models.Model):
    cust_name = models.CharField("Название", max_length=100, blank=True, null=True)

    def __unicode__(self):
        return smart_unicode(self.cust_name)

class CustomerLocation(models.Model):
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    location_name = models.CharField("Название", max_length=100, blank=True, null=True)
    location_adress = models.CharField("Адрес", max_length=100, blank=True, null=True)
    location_how_to_get = models.CharField("Как добраться", max_length=100, blank=True, null=True)

    def __unicode__(self):
        return smart_unicode(self.location_name)

class CustomerRepr(models.Model):
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    repr_last_name = models.CharField("Фамилия", max_length=100, blank=True, null=True)
    repr_name = models.CharField("Имя", max_length=100, blank=True, null=True)
    repr_patronymic = models.CharField("Отчество", max_length=100, blank=True, null=True)
    #tel_number = generic.GenericRelation(TelNumber, content_type_field=’entity_type’, object_id_field=’entity_id’)

    def __unicode__(self):
        return smart_unicode(self.repr_last_name)

def timesheet_upload_location(instance, filename):
    return "timesheets/%s/%s/%s" % (instance.sheet_date, instance.cust_location, filename)

class TimeSheet(models.Model):
    sheet_date = models.DateField("Дата", blank=True, null=True)
    sheet_turn = models.CharField("Смена", max_length=100, blank=True, null=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, blank=True, null=True)
    cust_location = models.ForeignKey(CustomerLocation, on_delete=models.CASCADE)#Автоматом подтягивать и имя заказчика
    foreman = models.ForeignKey(Worker, on_delete=models.CASCADE)
    customer_repr = models.ForeignKey(CustomerRepr, on_delete=models.CASCADE)
    turnouts_number = models.IntegerField("Количество рабочих", blank=True, null=True)
    image = models.ImageField(
        upload_to=timesheet_upload_location,
        null=True,
        blank=True,
        width_field='width_field',
        height_field='height_field')
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)

    def __unicode__(self):
        return smart_unicode(self.sheet_date)

class WorkerTurnout(models.Model):
    timesheet = models.ForeignKey(TimeSheet, on_delete=models.CASCADE)
    worker_id = models.ForeignKey(Worker, on_delete=models.CASCADE)
    worker_function = models.CharField(max_length=100, blank=True, null=True)
    hours_worked = models.DecimalField(max_digits=3, decimal_places=1)
