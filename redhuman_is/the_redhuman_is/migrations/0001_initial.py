# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-07 17:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_name', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('patronymic', models.CharField(max_length=100)),
                ('passport_number', models.CharField(max_length=9)),
                ('birth_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='WorkerMigrationCard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('series', models.IntegerField()),
                ('number', models.IntegerField()),
                ('worker_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='the_redhuman_is.Worker')),
            ],
        ),
        migrations.CreateModel(
            name='WorkerPassport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('another_passport_number', models.CharField(max_length=9)),
                ('date_of_issue', models.DateField()),
                ('date_of_exp', models.DateField()),
                ('issued_by', models.CharField(max_length=100)),
                ('worker_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='the_redhuman_is.Worker')),
            ],
        ),
        migrations.CreateModel(
            name='WorkerRegistration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=100)),
                ('street', models.CharField(max_length=100)),
                ('house_number', models.CharField(max_length=100)),
                ('building_number', models.CharField(max_length=100)),
                ('appt_number', models.CharField(max_length=100)),
                ('worker_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='the_redhuman_is.Worker')),
            ],
        ),
    ]
