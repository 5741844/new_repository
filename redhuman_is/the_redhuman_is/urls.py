from django.conf.urls import url

from . import views

app_name = 'the_redhuman_is'
urlpatterns = [

    url(r'^base/$', views.base, name='base'),

    url(r'^$', views.list_workers, name='list_workers'),
    url(r'^new-worker/$', views.new_worker, name='new_worker'),
    url(r'^worker/(?P<pk>[0-9]+)/$', views.worker_detail, name='worker_detail'),
    url(r'^worker/(?P<pk>[0-9]+)/edit/$', views.worker_edit, name='worker_edit'),
    url(r'^worker/(?P<pk>[0-9]+)/delete/$', views.worker_del, name='worker_del'),
    url(r'^worker/(?P<pk>[0-9]+)/new-passport/$', views.new_passport, name='new_passport'),
    url(r'^worker/(?P<pk>[0-9]+)/new-registration/$', views.new_registration, name='new_registration'),
    url(r'^worker/(?P<pk>[0-9]+)/image/$', views.worker_image, name='worker_image'),

    url(r'^customers/$', views.customers, name='customers'),
    url(r'^new-customer/$', views.new_customer, name='new_customer'),
    url(r'^customer/(?P<pk>[0-9]+)/$', views.customer_detail, name='customer_detail'),
    url(r'^customer/(?P<pk>[0-9]+)/new-locations/$', views.new_locations, name='new_locations'),
    url(r'^customer/(?P<pk>[0-9]+)/new-representatives/$', views.new_representatives, name='new_representatives'),

    url(r'^new-timesheet/$', views.new_timesheet, name='new_timesheet'),
    url(r'^timesheets/$', views.timesheets, name='timesheets'),
    url(r'^timesheet/(?P<pk>[0-9]+)/$', views.timesheet, name='timesheet'),
    url(r'^timesheet/(?P<pk>[0-9]+)/image/$', views.timesheet_image, name='timesheet_image'),
    url(r'^timesheet/(?P<pk>[0-9]+)/new-turnouts/$', views.new_turnouts, name='new_turnouts'),

]
