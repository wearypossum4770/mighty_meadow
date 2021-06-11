from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, render

from appointments.forms import AppointmentForm
from appointments.models import Appointment, Patient

User = get_user_model()


def user_is_authorized_party(user):
    is_authorized_party = Patient.objects.get(patient_id=user.id)
    return is_authorized_party
    is_patient = User.objects.get(username=user.username)
    return is_patient


def user_is_authorized_party(user):
    Patient.objects.get()
    patient = Patient.objects.get(owner=user.id)
    return


def user_is_authenticated(user):
    return user.is_authenticated


@login_required
@user_passes_test(user_is_authenticated)
def create_appointment_patient_id(request, patient_id):
    obj, created = Appointment.objects.get_or_create(
        patient_id=patient_id,
        scheduler_id=request.user.id,
        location=request.POST.get('location'),
        start_time=request.POST.get('start_time'),
        end_time=request.POST.get('end_time'),
    )
    if created:
        return JsonResponse({"created": created})
    # if request.user.is_authenticated:
    #     form = AppointmentForm(request.POST)
    #     if request.method == "POST":
    #         if form.is_valid():
    #             form.save()
    # return HttpResponse(form)
    # appt = Appointment.objects.create()


def appointment_details(request, appointment_id):
    appointment = get_object_or_404(Appointment, pk=appointment_id)
    if appointment.patient.username == request.user.username:
        return JsonResponse(
            {
                "patient": appointment.patient.username,
                "scheduler": appointment.scheduler.username,
                "scheduled_time": appointment.scheduled_time,
                "start_time": appointment.start_time,
                "end_time": appointment.end_time,
                "location": appointment.location,
                "action_status": appointment.action_status,
            }
        )


def archive(request):
    context = {}
    return JsonResponse(context)


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
