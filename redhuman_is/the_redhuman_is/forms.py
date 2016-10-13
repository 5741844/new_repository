
# -*- coding: utf-8 -*-
from django import forms
from .models import Worker

class WorkerForm(forms.ModelForm):

    class Meta:
        model = Worker
        fields = ('last_name', 'name', 'patronymic', 'passport_number', 'birth_date', 'mig_series', 'mig_number', 'm_date_of_issue', 'm_date_of_exp',)
