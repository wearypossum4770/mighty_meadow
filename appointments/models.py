from datetime import datetime
from uuid import uuid4

from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models import (
    CASCADE,
    BooleanField,
    CharField,
    DateTimeField,
    EmailField,
    FileField,
    ForeignKey,
    ImageField,
    IntegerField,
    Model,
    TextChoices,
    TextField,
    UUIDField,
)
from django.utils.translation import gettext_lazy as _

BASE_DIR = settings.BASE_DIR
userModel = settings.AUTH_USER_MODEL
User = get_user_model()


def wrap_up_time():
    ...


def after_call_work():
    ...


def disposition_code():
    ...


# https://www.callcentrehelper.com/tag/workforce-management
# class ConatctLog(Model):
#     class Disposition(TextChoices):
#         ABANDONED = "", _("Caller abandoned in queue")
#         SCHEDULED = "SCH", _("Caller qppointment scheduled")
#         BUSY= "BSY", _("Line Busy")
#         CALLBACK= "CBK", _("Caller request, callback")
#         COMPLAINT = "CMP", _("Caller wishes to file Complaint/Greievnance")
#         COMPLETE = "CPT"
# class Type:
#     INBOUND
#     OUTBOUND
#     WARM_TRANSFER
#     COLD_TRANSFER
# class NextAction:
# outcome = CharField(max_length=100, null=True, blank=True)

# Complete
# Disconnected number
# Incorrect number
# Not interested
# Product question
# Requires follow up
# Requires supervisor attention


# Tech support
class Patient(Model):
    """
    United States Census Beurau Ethnicity Information. https://www.census.gov/topics/population/race/about.html
    Improved Ethinicity Information. https://www2.census.gov/cac/nac/meetings/2016-10/2016-nac-jones.pdf
    """

    class Gender(TextChoices):
        MALE = "M", _(
            "I identify as a male or a man (i.e. male, cis-gender male), and prefer to be called sir"
        )
        FEMALE = "F", _(
            "I identify as a female or a woman (i.e. female, cis-gender female),  and prefer to be called ma'am."
        )
        TRANSGENDER_FEMALE = "MTF", _(
            "Assigned male at birth, but currently identify as female."
        )
        TRANSGENDER_MALE = "FTM", _(
            "Assigned female at birth but currently identify as male."
        )
        NON_BINARY = "NBN", _("Neither male nor female, somewhere in between.")
        __empty__ = _("No Selection, Declined To Answer")

    class Ethnicity(TextChoices):
        ASIAN = "ASN", _(
            "Asian - Far East, Southeast Asia, or the Indian subcontinent including, for example, Cambodia, China, India, Japan, Korea, Malaysia, Pakistan, the Philippine Islands, Thailand, and Vietnam."
        )
        BLACK = "BLK", _(
            "Black - origins in any of the Black racial groups of Africa including Carribean Islands."
        )
        Native = "NAT", _("Native American or Alaskan Native.")
        HISPANIC = "HPN", _(
            "Hispanic - Centeral and South America, Carribbean Islands."
        )
        MIDDLE_EASTERN = "MDE", _("Middle Eastern - the Middle East, or North Africa.")
        HAWAIIAN = "HWN", _("Native Hawaii, Guam, Samoa, or other Pacific Islands.")
        OTHER = "OTH", _("Other/Multiple")
        WHITE = "WHT", _("White-origins in Europe.")
        __empty__ = _("No Selection, Declined To Answer")

    owner = ForeignKey(
        User, on_delete=CASCADE, null=True, blank=True, related_name="patient"
    )
    sponsor = ForeignKey(User, on_delete=CASCADE, related_name="guarantor")
    gender = CharField(
        max_length=3,
        choices=Gender.choices,
        default=Gender.__empty__,
    )
    ethnicity = CharField(
        max_length=3, choices=Ethnicity.choices, default=Ethnicity.__empty__
    )


class Appointment(Model):
    patient = ForeignKey(Patient, on_delete=CASCADE)
    scheduler = ForeignKey(User, on_delete=CASCADE)


# ADMIN = "ADMIN", _("Administration")
# AGRMT = "AGRMT", _("Agreement")
# AOF = "AOF", _("Address on File")
# AOS = "AOS", _("Already on System")
# APVL = "APVL", _("Approval")
# ATTM = "ATTM", _("At this time")
# AUTH = "AUTH", _("Authority, authorise")
# CB = "CB", _("or CL BK, Call back")
# CC = "CC", _("Customer care")
# CCI = "CCI", _("Customer called in")
# CIN = "CIN", _("Customer I/D number")
# CCM = "CCM", _("Customer Care Manager")
# CMPLT = "CMPLT", _("Complete")
# CNL = "CNL", _("Cancel")
# CONF = "CONF", _("Confidential")
# COT = "COT", _("Change of title")
# CSM = "CSM", _("Customer Service Manager")
# CTI = "CTI", _("Customer telephoned in")
# CUST = "CUST", _("Customer")
# CUST_SUPP = "CUST_SUPP", _("Customer Support")
# DD = "DD", _("Direct debit")
# DESTN = "DESTN", _("Destination")
# DET = "DET", _("Detail(s)")
# DLVY = "DLVY", _("Delivery")
# DPA = "DPA", _("Data Protection Act")
# EDD = "EDD", _("Expected date of delivery")
# EMERG = "EMERG", _("Emergency")
# ENRT = "ENRT", _("En route")
# EST = "EST", _("Estimate or estimation")
# EVAL = "EVAL", _("Evaluate or evaluation")
# EXTN = "EXTN", _("Extension")
# FAO = "FAO", _("For attention of")
# FONE = "FONE", _("Telephone")
# FTE = "FTE", _("Full-time equivalent")
# IAW = "IAW", _("In accordance with")
# IDENT = "IDENT", _("Identify or identifier or identification")
# IMPT = "IMPT", _("Important")
# IMT = "IMT", _("Immediate or immediately")
# INFO = "INFO", _("Information")
# K = "K", _("Thousand")
# MAX = "MAX", _("Maximum")
# MISG = "MISG", _("Missing")
# MULT = "MULT", _("Multiple")
# NA = "N/A", _("Not applicable")
# NAP = "NAP", _("Not at present")
# NC = "NC", _("No change")
# NIS = "NIS", _("Not in system")
# NOAC = "NOAC", _("No action necessary")
# NOFIN = "NOFIN", _("No further information")
# NT = "NT", _("No trace")
# ON_file = "O/F", _("On file")
# OVERPAYMENT = "O/P", _("Overpayment")
# ON_request = "O/R", _("On request")
# OTS = "OTS", _("Out of service")
# PH = "PH", _("Past history")
# PI = "PI", _("Personal issue")
# PO = "PO", _("Purchase order")
# PYT = "PYT", _("Payment")
# QLTY = "QLTY", _("Quality")
# QNTY = "QNTY", _("Quantity")
# RECD = "RECD", _("Received")
# RE = "RE", _("In regard to")
# REQD = "REQD", _("Required")
# REQSTD = "REQSTD", _("Requested")
# RETN = "RETN", _("Return/Returned")
# RFC = "RFC", _("Request for change")
# RPRT = "RPRT", _("Report")
# SATFY = "SATFY", _("Satisfy or satisfactory")
# SC = "SC", _("Sort Code")
# SDBY = "SDBY", _("Standby")
# SGD = "SGD", _("Signed")
# SLA = "SLA", _("Service Level Agreement")
# SO = "SO", _("Standing order")
# SP = "SP", _("Single payment")
# SUP = "SUP", _("Supply")
# SUSP = "SUSP", _("Suspend")
# SYS = "SYS", _("System")
# TEMP = "TEMP", _("Temporary")
# TOC = "TOC", _("To be continued")
# TOD = "TOD", _("Time of delivery")
# TOR = "TOR", _("Time of receipt")
# TRANSCODE = "TRANSCODE", _("Transaction code")
# TRMT = "TRMT", _("Terminate")
# UNAPV = "UNAPV", _("Unable to approve")
# UNAVBL = "UNAVBL", _("Unavailable")
# UNDLD = "UNDLD", _("Undelivered")
# URG = "URG", _("Urgent")
# UNSATFY = "UNSATFY", _("Unsatisfactory")
# WEF = "WEF", _("With effect from")
# WIBIS = "WIBIS", _("Will be issued")
# WIP = "WIP", _("Work in progress")
# WISMO = "WISMO", _("Where is my order?")
