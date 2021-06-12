from django.urls import path

from appointments.views import (
    api_create_appointment_patient_id,
    appointment_details,
    archive,
    view_appointment,
)

urlpatterns = [
    path("appointments/<appointment_id>/", appointment_details, name="appt-detail"),
    path(
        "appointments/schedule-appointment/<int:patient_id>",
        api_create_appointment_patient_id,
        name="new-appt",
    ),
    path("appointments/", view_appointment, name="appt-list"),
]
