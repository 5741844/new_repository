# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic

from .models import Worker, TelNumber
# Create your views here.
class IndexView(generic.ListView):
    template_name = 'the_redhuman_is/index.html'
    context_object_name = 'latest_worker_list'

    def get_queryset(self):
        """Return the last five published Workers."""
        return Worker.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Worker
    template_name = 'the_redhuman_is/detail.html'


class ResultsView(generic.DetailView):
    model = Worker
    template_name = 'the_redhuman_is/results.html'

def vote(request, worker_id):
    worker = get_object_or_404(Worker, pk=worker_id)
    try:
        selected_telnumber = worker.telnumber_set.get(pk=request.POST['telnumber'])
    except (KeyError, TelNumber.DoesNotExist):
        # Redisplay the Worker voting form.
        return render(request, 'the_redhuman_is/detail.html', {
            'worker': worker,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_telnumber.votes += 1
        selected_telnumber.save()
        return HttpResponseRedirect(reverse('the_redhuman_is:results', args=(worker.id,)))
