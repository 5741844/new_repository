
# -*- coding: utf-8 -*-
from django import forms
from django.forms import ModelForm, DateInput, DateField, formset_factory, modelformset_factory, ChoiceField, Select
from .models import Worker, WorkerPassport, WorkerRegistration, Customer, CustomerLocation, CustomerRepr, TimeSheet, WorkerTurnout

class WorkerForm(forms.ModelForm):
    birth_date = DateField(input_formats=['%d.%m.%Y'], required=False, help_text="Формат ввода: <em>дд.мм.гггг</em>")
    m_date_of_issue = DateField(input_formats=['%d.%m.%Y'])
    m_date_of_exp = DateField(input_formats=['%d.%m.%Y'])
    class Meta:
        model = Worker
        fields = (
        'last_name',
        'name',
        'patronymic',
        'passport_number',
        'birth_date',
        'mig_series',
        'mig_number',
        'm_date_of_issue',
        'm_date_of_exp',
        'image1',
        'image2',
        'image3',
        )

class WorkerPassportForm(forms.ModelForm):
    date_of_issue = DateField(input_formats=['%d.%m.%Y'])
    date_of_exp = DateField(input_formats=['%d.%m.%Y'])
    class Meta:
        model = WorkerPassport
        fields = (
        'passport_type',
        'another_passport_number',
        'date_of_issue',
        'date_of_exp',
        'issued_by',
        )

class WorkerRegistrationForm(forms.ModelForm):
    class Meta:
        model = WorkerRegistration
        fields = (
        'city',
        'street',
        'house_number',
        'building_number',
        'appt_number',
        )

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('cust_name',)

class TimeSheetForm(forms.ModelForm):
    sheet_date = DateField(input_formats=['%d.%m.%Y'])
    class Meta:
        model = TimeSheet
        fields = (
        'sheet_date',
        'sheet_turn',
        'customer',
        'cust_location',
        'customer_repr',
        'foreman',
        'turnouts_number',
        'image',
        )

CustomerLocationFormSet = modelformset_factory(CustomerLocation, fields=(
'location_name',
'location_adress',
'location_how_to_get',
))

CustomerReprFormSet = modelformset_factory(CustomerRepr, fields=(
'repr_last_name',
'repr_name',
'repr_patronymic',
))

WorkerTurnoutFormSet = modelformset_factory(WorkerTurnout, fields=(
'worker_id',
'worker_function',
'hours_worked',
))
