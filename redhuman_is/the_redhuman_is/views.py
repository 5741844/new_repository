# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.db.models import Count

from .models import Worker, WorkerPassport, WorkerRegistration, Customer, CustomerLocation, CustomerRepr, TimeSheet, WorkerTurnout
from .forms import WorkerForm, WorkerPassportForm, WorkerRegistrationForm, CustomerForm, CustomerReprFormSet, CustomerLocationFormSet, TimeSheetForm, WorkerTurnoutFormSet
# Create your views here.
@login_required
def base(request):
    return render(request, 'the_redhuman_is/base.html', {})

@login_required
def new_worker(request):
    if request.method == "POST":
        wform = WorkerForm(request.POST, request.FILES)
        wpform = WorkerPassportForm(request.POST)
        wrform = WorkerRegistrationForm(request.POST)
        if wform.is_valid() and wpform.is_valid():
            worker = wform.save(commit=False)
            worker.input_date = timezone.now()
            worker.save()
            workerregistration = wrform.save(commit=False)
            workerpassport = wpform.save(commit=False)
            workerpassport.workers_id = worker
            workerregistration.workers_id = worker
            workerregistration.save()
            workerpassport.save()
            return redirect('/')
    else:
        wform = WorkerForm()
        wpform = WorkerPassportForm()
        wrform = WorkerRegistrationForm()
    return render(request, 'the_redhuman_is/new_worker.html', {'wform': wform, u'wpform': wpform, 'wrform': wrform})

@login_required
def worker_image(request, pk):
    instance = get_object_or_404(Worker, pk=pk)
    return render(request, 'the_redhuman_is/image.html', {u'instance': instance})

@login_required
def list_workers(request):
    workers = Worker.objects.annotate(Count('workerturnout')).order_by('-input_date')
    return render(request, 'the_redhuman_is/list_workers.html', {'workers': workers})

@login_required
def worker_detail(request, pk):
    worker = get_object_or_404(Worker, pk=pk)
    workerpasss = Worker.objects.get(pk=pk).workerpassport_set.all()
    workerregs = Worker.objects.get(pk=pk).workerregistration_set.all()
    turnouts = Worker.objects.get(pk=pk).workerturnout_set.all()
    timesheets = TimeSheet.objects.filter(workerturnout__worker_id=pk)
    return render(request, 'the_redhuman_is/worker_detail.html', {u'worker': worker, u'workerpasss': workerpasss, u'workerregs': workerregs, 'turnouts': turnouts, 'timesheets': timesheets})

@login_required
def worker_edit(request, pk):
    worker = get_object_or_404(Worker, pk=pk)
    if request.method == "POST":
        form = WorkerForm(request.POST, instance=worker)
        if form.is_valid():
            worker = form.save(commit=False)
            worker.input_date = timezone.now()
            worker.save()
            return redirect('/list-workers/')
    else:
        form = WorkerForm(instance=worker)
    return render(request, 'the_redhuman_is/new_worker.html', {'form': form})

@login_required
def worker_del(request, pk):
        worker = get_object_or_404(Worker, pk=pk)
        if request.method == "POST":
            form = WorkerForm(request.POST, instance=worker)
            if form.is_valid():
                worker.delete()
                return redirect('/list-workers/')
        else:
            form = WorkerForm(instance=worker)
        return render(request, 'the_redhuman_is/new_worker.html', {'form': form})

@login_required
def new_passport(request, pk):
    #customer = Customer.objects.get(pk=pk)
    worker = get_object_or_404(Worker, pk=pk)
    if request.method == "POST":
        npform = WorkerPassportForm(request.POST)
        if npform.is_valid():
            passport = npform.save(commit=False)
            passport.workers_id = worker
            passport.save()
            return redirect('/list-workers/')
    else:
        npform = WorkerPassportForm()
    return render(request, 'the_redhuman_is/new_passport.html', {'npform': npform})

@login_required
def new_registration(request, pk):
    #customer = Customer.objects.get(pk=pk)
    worker = get_object_or_404(Worker, pk=pk)
    if request.method == "POST":
        nrform = WorkerRegistrationForm(request.POST)
        if nrform.is_valid():
            registration = nrform.save(commit=False)
            registration.workers_id = worker
            registration.save()
            return redirect('/list-workers/')
    else:
        nrform = WorkerRegistrationForm()
    return render(request, 'the_redhuman_is/new_registration.html', {'nrform': nrform})

@login_required
def customers(request):
    customers = Customer.objects.order_by('cust_name')
    return render(request, 'the_redhuman_is/customers.html', {'customers': customers})

@login_required
def new_customer(request):
    if request.method == "POST":
        cform = CustomerForm(request.POST)
        if cform.is_valid():
            customer = cform.save(commit=False)
            customer.save()
            return redirect('/customers/')
    else:
        cform = CustomerForm()
    return render(request, 'the_redhuman_is/new_customer.html', {'cform': cform})

@login_required
def customer_detail(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    customerlocs = Customer.objects.get(pk=pk).customerlocation_set.all()
    customerreprs = Customer.objects.get(pk=pk).customerrepr_set.all()
    return render(request, 'the_redhuman_is/customer_detail.html', {u'customer': customer, 'customerlocs': customerlocs, 'customerreprs': customerreprs})

@login_required
def new_locations(request, pk):
    #customer = Customer.objects.get(pk=pk)
    customer = get_object_or_404(Customer, pk=pk)
    if request.method == "POST":
        formset = CustomerLocationFormSet(request.POST)
        if formset.is_valid():
            customerlocations = formset.save(commit=False)
            for customerlocation in customerlocations:
                customerlocation.customer_id = customer
                customerlocation.save()
            return redirect('/customers/')
    else:
        formset = CustomerLocationFormSet()
    return render(request, 'the_redhuman_is/new_locations.html', {'formset': formset})

@login_required
def new_representatives(request, pk):
    #customer = Customer.objects.get(pk=pk)
    customer = get_object_or_404(Customer, pk=pk)
    if request.method == "POST":
        formset = CustomerReprFormSet(request.POST)
        if formset.is_valid():
            customerreprs = formset.save(commit=False)
            for customerrepr in customerreprs:
                customerrepr.customer_id = customer
                customerrepr.save()
            return redirect('/customers/')
    else:
        formset = CustomerReprFormSet()
    return render(request, 'the_redhuman_is/new_representatives.html', {'formset': formset})

@login_required
def new_timesheet(request):
    if request.method == "POST":
        tform = TimeSheetForm(request.POST, request.FILES or None)
        if tform.is_valid():
            timesheet = tform.save(commit=False)
            timesheet.save()
            return redirect('/timesheets/')
    else:
        tform = TimeSheetForm()
    return render(request, 'the_redhuman_is/new_timesheet.html', {u'tform': tform})

@login_required
def timesheets(request):
    timesheets = TimeSheet.objects.order_by('-sheet_date')
    return render(request, 'the_redhuman_is/timesheets.html', {'timesheets': timesheets})

@login_required
def timesheet(request, pk):
    timesheet = get_object_or_404(TimeSheet, pk=pk)
    turnouts = TimeSheet.objects.get(pk=pk).workerturnout_set.all()
    return render(request, 'the_redhuman_is/timesheet.html', {u'timesheet': timesheet, 'turnouts': turnouts})

@login_required
def timesheet_image(request, pk):
    instance = get_object_or_404(TimeSheet, pk=pk)
    return render(request, 'the_redhuman_is/image.html', {u'instance': instance})


@login_required
def new_turnouts(request, pk):
        timesheet = get_object_or_404(TimeSheet, pk=pk)
        if request.method == "POST":
            formset = WorkerTurnoutFormSet(request.POST)
            if formset.is_valid():
                workerturnouts = formset.save(commit=False)
                for workerturnout in workerturnouts:
                    workerturnout.timesheet = timesheet
                    workerturnout.save()
                return redirect('/timesheets/')
        else:
            formset = WorkerTurnoutFormSet()
            formset.extra = TimeSheet.objects.get(pk=pk).turnouts_number #values('turnouts_number')
        return render(request, 'the_redhuman_is/new_turnouts.html', {'formset': formset})
