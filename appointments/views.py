from asgiref.sync import sync_to_async
from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, render

from appointments.forms import AppointmentForm
from appointments.models import Appointment, Patient

User = get_user_model()


def user_can_manage_me(user):
    return user.has_perm("your_app.manage_object")


def user_is_authenticated(user):
    return user.is_authenticated


def user_is_patient(user):
    return user.is_patient


def user_is_clinic_staff(user):
    return user.is_clinic_staff


@login_required
@user_passes_test(user_is_authenticated)
def api_create_appointment_by_patient_id(request, patient_id):
    context = {}
    patient = Patient.objects.get(owner=patient_id)
    user_is_authorized_party = len(
        [
            user.username
            for user in patient.authorized_party.all()
            if user.username == request.user.username
        ]
    )
    if user_is_authorized_party:
        obj, created = Appointment.objects.get_or_create(
            patient_id=patient_id,
            scheduler_id=request.user.id,
            location=request.POST.get("location"),
            start_time=request.POST.get("start_time"),
            end_time=request.POST.get("end_time"),
        )
        # if not obj.user_can_manage_me(request.user):
        if created:
            context.update(
                created=created,
                user_is_authorized_party=user_is_authorized_party,
                status_code=201,
                appointment_details={
                    "visit_identifier": obj.visit_identifier,
                    "scheduled_time": obj.scheduled_time,
                    "start_time": obj.start_time,
                    "end_time": obj.end_time,
                    "location": obj.location,
                    "action_status": obj.action_status,
                },
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


@login_required
@user_passes_test(user_is_authenticated)
def api_appointment_details(request, appointment_id):
    ...


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
def view_appointments(request):
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
                "external_identifier": a.external_identifier,
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


#  cancel_appointment_by_date_range
#  cancel_appointment_by_appointment_id
#  appointment_modification_notify_patient
#  create_appointment_by_patient_id
#  create_appointment_by_system
#  view_appointment_details_by_appointment_id
#  view_appointment_list_by_patient_id
#  view_appointment_list_by_date_range
#  view_current_day_appointment_list
#
