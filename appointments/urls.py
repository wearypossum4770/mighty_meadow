from django.urls import path

from appointments.views import (
    appointment_detail,
    archive,
    create_appointment_patient_id,
    view_appointment,
)

urlpatterns = [
    path("appointments/<appointment_id>/", appointment_detail, name="appt-detail"),
    path("appointments/schedule-appointment/<int:patient_id>", create_appointment_patient_id, name="new-appt"),
    path("appointments/", view_appointment, name="appt-list"),
]
