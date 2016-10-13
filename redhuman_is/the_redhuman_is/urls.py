from django.conf.urls import url

from . import views

app_name = 'the_redhuman_is'
urlpatterns = [

    url(r'^$', views.base, name='base'),
    url(r'^new-worker/$', views.new_worker, name='new_worker'),
    url(r'^add-worker/$', views.add_worker, name='add_worker'),
    url(r'^list-workers/$', views.list_workers, name='list_workers'),
    url(r'^worker/(?P<pk>[0-9]+)/$', views.worker_detail, name='worker_detail'),
]
