from django.urls import path

from appointments.views import (
    api_create_appointment_by_patient_id,
    appointment_details,
    archive,
    cancel_appointment_by_appointment_id,
    view_appointments,
)

urlpatterns = [
    path(
        "appointments/<appointment_id/cancel/",
        cancel_appointment_by_appointment_id,
        name="appt-cancel",
    ),
    path("appointments/<appointment_id>/", appointment_details, name="appt-detail"),
    path(
        "appointments/schedule-appointment/<int:patient_id>",
        api_create_appointment_by_patient_id,
        name="new-appt",
    ),
    path("appointments/", view_appointments, name="appt-list"),
]
