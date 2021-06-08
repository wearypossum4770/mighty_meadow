from django.urls import path

from appointments.views import view_appointment

urlpatterns = [path("appointments/", view_appointment, name="appt-list")]
