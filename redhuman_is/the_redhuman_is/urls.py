from django.conf.urls import url

from . import views

app_name = 'the_redhuman_is'
urlpatterns = [

    url(r'^$', views.base, name='base'),
    url(r'^new-worker/$', views.new_worker, name='new_worker'),
    url(r'^list-workers/$', views.list_workers, name='list_workers'),
    url(r'^worker/(?P<pk>[0-9]+)/$', views.worker_detail, name='worker_detail'),
    url(r'^worker/(?P<pk>[0-9]+)/edit/$', views.worker_edit, name='worker_edit'),
    url(r'^worker/(?P<pk>[0-9]+)/delete/$', views.worker_del, name='worker_del'),
    url(r'^customers/$', views.customers, name='customers'),
    url(r'^new-customer/$', views.new_customer, name='new_customer'),
    url(r'^customer/(?P<pk>[0-9]+)/$', views.customer_detail, name='customer_detail'),
    url(r'^customer/(?P<pk>[0-9]+)/new-locations/$', views.new_locations, name='new_locations'),
    url(r'^customer/(?P<pk>[0-9]+)/new-representatives/$', views.new_representatives, name='new_representatives'),
]
