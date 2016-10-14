# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone



from .models import Worker, WorkerPassport, WorkerRegistration
from .forms import WorkerForm, WorkerPassportForm, WorkerRegistrationForm
# Create your views here.
def base(request):
    return render(request, 'the_redhuman_is/base.html', {})

def new_worker(request):
    if request.method == "POST":
        wform = WorkerForm(request.POST)
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
            return redirect('/list-workers/')
    else:
        wform = WorkerForm()
        wpform = WorkerPassportForm()
        wrform = WorkerRegistrationForm()
    return render(request, 'the_redhuman_is/new_worker.html', {'wform': wform, u'wpform': wpform, 'wrform': wrform})

def list_workers(request):
    workers = Worker.objects.order_by('-input_date')
    return render(request, 'the_redhuman_is/list_workers.html', {'workers': workers})

def worker_detail(request, pk):
    worker = get_object_or_404(Worker, pk=pk)
    q_worker = Worker.objects.get(pk=pk)
    workerpass = get_object_or_404(q_worker.workerpassport_set)
    workerreg = get_object_or_404(q_worker.workerregistration_set)
    return render(request, 'the_redhuman_is/worker_detail.html', {u'worker': worker, u'workerpass': workerpass, u'workerreg': workerreg})

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
