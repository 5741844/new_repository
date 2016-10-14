
# -*- coding: utf-8 -*-
from django import forms
from django.forms import ModelForm, DateInput, DateField
from .models import Worker, WorkerPassport, WorkerRegistration


class WorkerForm(forms.ModelForm):
    birth_date = DateField(input_formats=['%d.%m.%Y'], required=False, help_text="Формат ввода: <em>дд.мм.гггг</em>")
    m_date_of_issue = DateField(input_formats=['%d.%m.%Y'])
    m_date_of_exp = DateField(input_formats=['%d.%m.%Y'])
    class Meta:
        model = Worker
        fields = ('last_name', 'name', 'patronymic', 'passport_number', 'birth_date', 'mig_series', 'mig_number', 'm_date_of_issue', 'm_date_of_exp',)
        #widgets = {
            #'birth_date': DateInput(format='%d.%m.%Y'),
            #'m_date_of_issue': DateInput(format='%d.%m.%Y'),
            #'m_date_of_exp': DateInput(format='%d.%m.%Y')
        #}
class WorkerPassportForm(forms.ModelForm):
    date_of_issue = DateField(input_formats=['%d.%m.%Y'])
    date_of_exp = DateField(input_formats=['%d.%m.%Y'])
    class Meta:
        model = WorkerPassport
        fields = ('passport_type', 'another_passport_number', 'date_of_issue', 'date_of_exp', 'issued_by',)

class WorkerRegistrationForm(forms.ModelForm):
    class Meta:
        model = WorkerRegistration
        fields = ('city', 'street', 'house_number', 'building_number', 'appt_number')
