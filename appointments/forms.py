from django.forms import EmailField, ModelForm

from appointments.models import Appointment


class AppointmentForm(ModelForm):
    class Meta:
        model = Appointment
        fields = (
            "patient",
            "start_time",
            "end_time",
            "location",
        )
