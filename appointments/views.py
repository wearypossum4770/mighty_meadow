from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponse, JsonResponse
from django.http.response import Http404
from django.shortcuts import get_object_or_404, render

from appointments.forms import AppointmentForm
from appointments.models import Appointment, Patient

User = get_user_model()


def user_can_manage_me(user):
    return user.has_perm("your_app.manage_object")


def user_is_authenticated(user):
    return user.is_authenticated


@login_required
@user_passes_test(user_is_authenticated)
def api_create_appointment_patient_id(request, patient_id):
    context = {}
    if request.user.is_anonymous:
        context.update(created=False)
    patient = Patient.objects.get(owner=patient_id)
    authorized_parties = [user.username for user in patient.authorized_party.all()]
    user_is_authorized_party = False
    for party in authorized_parties:
        if party == request.user.username:
            user_is_authorized_party = True
    if user_is_authorized_party:
        obj, created = Appointment.objects.get_or_create(
            patient_id=patient_id,
            scheduler_id=request.user.id,
            location=request.POST.get("location"),
            start_time=request.POST.get("start_time"),
            end_time=request.POST.get("end_time"),
        )
        # if not obj.user_can_manage_me(request.user):
        if created and user_is_authorized_party:
            context.update(
                created=created,
                user_is_authorized_party=user_is_authorized_party,
            )
    return JsonResponse(context)


@login_required
@user_passes_test(user_is_authenticated)
def create_appointment_patient_id(request, patient_id):

    header = {"X-Status-Reason": "Validation failed"}
    form = AppointmentForm(request.POST)
    print(form.instance)
    if request.method == "POST":
        if form.is_valid():
            form.save()
    return HttpResponse(form)


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
