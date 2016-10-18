from django.contrib import admin

from . models import Worker, WorkerPassport, WorkerRegistration, Customer, CustomerLocation, CustomerRepr, TimeSheet, WorkerTurnout

# Register your models here.
admin.site.register(Worker)
admin.site.register(WorkerPassport)
admin.site.register(WorkerRegistration)
admin.site.register(Customer)
admin.site.register(CustomerLocation)
admin.site.register(CustomerRepr)
admin.site.register(TimeSheet)
