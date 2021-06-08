from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import JsonResponse
from django.shortcuts import render

from appointments.models import Appointment


@login_required
def view_appointment(request):
    # check against user
    context = {}
    if request.user.is_authenticated:
        context["appointment_list"] = [
            {
                "scheduled_time": a.scheduled_time,
                "start_time": a.start_time,
                "end_time": a.end_time,
                "location": a.location,
                "action_status": a.action_status,
            }
            for a in Appointment.objects.filter(patient=request.user.id)
        ]
    print(request)

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
