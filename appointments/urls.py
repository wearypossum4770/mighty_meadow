from django.urls import path

from appointments.views import create_appointment, view_appointment

urlpatterns = [
    path("schedule-appointment/", create_appointment, name="new-appt"),
    path("appointments/", view_appointment, name="appt-list"),
]
