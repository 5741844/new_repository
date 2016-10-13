# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone


from .models import Worker
from .forms import WorkerForm
# Create your views here.
def base(request):
    return render(request, 'the_redhuman_is/base.html', {})

def new_worker(request):
    if request.method == "POST":
        form = WorkerForm(request.POST)
        if form.is_valid():
            worker = form.save(commit=False)
            worker.input_date = timezone.now()
            worker.save()
            return redirect('/')
    else:
        form = WorkerForm()
    return render(request, 'the_redhuman_is/new_worker.html', {'form': form})

def add_worker(request):
    return render(request, 'the_redhuman_is/add_worker.html', {})

def list_workers(request):
    workers = Worker.objects.order_by('-input_date')
    return render(request, 'the_redhuman_is/list_workers.html', {'workers': workers})

def worker_detail(request, pk):
    worker = get_object_or_404(Worker, pk=pk)
    return render(request, 'the_redhuman_is/worker_detail.html', {'worker': worker})
