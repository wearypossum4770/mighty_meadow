from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

from appointments.forms import AppointmentForm
from appointments.models import Appointment


@login_required
def create_appointment(request):
    form = AppointmentForm(request.POST)
    print(request.POST)
    return HttpResponse(form)
    # appt = Appointment.objects.create()


@login_required
def view_appointment(request):
    # check against user
    context = {}
    appt = Appointment.objects.filter(patient=request.user.id)
    if request.user.is_authenticated:
        context["appointment_list"] = [
            {
                "scheduled_time": a.scheduled_time,
                "start_time": a.start_time,
                "end_time": a.end_time,
                "location": a.location,
                "action_status": a.action_status,
            }
            for a in appt
        ]
    return JsonResponse(context)


def authorized_for_account(user):

    return


@user_passes_test(authorized_for_account)
@login_required
def make_appointment(request):
    context = {}
    if request.user.is_authenticated:
        print(request)
    return JsonResponse(context)
