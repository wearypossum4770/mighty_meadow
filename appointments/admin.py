from django.contrib import admin

from appointments.models import Appointment, Patient

admin.site.register(Appointment)
admin.site.register(Patient)
