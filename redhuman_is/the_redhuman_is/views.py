from django.shortcuts import render
from django.http import HttpResponse

from .models import Worker

from django.template import RequestContext, loader
# Create your views here.
def index(request):
    latest_worker_list = Worker.objects.order_by('-input_date')[:5]
    template = loader.get_template('the_redhuman_is/index.html')
    context = RequestContext(request, {
        'latest_worker_list': latest_worker_list,
    })
    return HttpResponse(template.render(context))

def detail(request, worker_id):
    return HttpResponse("You're looking at worker %s." % worker_id)

def results(request, worker_id):
    response = "You're looking at the results of worker %s."
    return HttpResponse(response % worker_id)

def vote(request, worker_id):
    return HttpResponse("You're voting on worker %s." % worker_id)
