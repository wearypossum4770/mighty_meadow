from cuid import cuid
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from users.forms import ProfileUpdateForm, UserRegisterForm, UserUpdateForm
from users.models import Address, Profile

address_switcher = {
        "MAIL": "Mailing",
        "RESD": "Residential",
        "BUSN": "Business",
    }
def create_address(street1, street2, state, city, zipcode, *args, **kwargs):
    address = Address.objects.create(
        street1=street1,
        street2=street2,
        state=state,
        city=city,
        zipcode=zipcode,
    )
    ...


def read_address(*args, **kwargs):
    ...


def update_address(*args, **kwargs):
    ...


def homepage(request):
    return render(request, "users/home.html")


def about(request):
    return render(request, "users/about.html")


def change_address(user=None, *args, **kwargs):
    address_switcher = {
        "MAIL": "Mailing",
        "RESD": "Residential",
        "BUSN": "Business",
    }
    print(args)
    print(kwargs)


def create_registration(*args, **kwargs):
    user = get_user_model().objects.create_user(
        first_name=kwargs.get("first_name"),
        middle_name=kwargs.get("middle_name"),
        last_name=kwargs.get("last_name"),
        password=kwargs.get("password"),
        email=kwargs.get("email"),
        username=kwargs.get("username"),
    )
    # profile =Profile.objects.create()
    ...


def update_registration(*args, **kwargs):
    ...


def registration(request):
    form = UserRegisterForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(
                request, f"Your account has been created! You are now able to log in"
            )
            return redirect("login")
    return render(request, "users/register.html", {"form": form})


@login_required
def profile(request):
    address = change_address({"user": request.user})
    addr = Profile.objects.get().addresses.all()
    addresses = [
        {
            "idempotent_key": address.idempotent_key,
            "address_type": address_switcher.get(address.address_type),
            "street1": address.street1,
            "street2": address.street2,
            "state": address.state,
            "city": address.city,
            "zipcode": address.zipcode,
        }
        for address in addr
    ]
    user_form = UserUpdateForm(request.POST, instance=request.user)
    profile_form = ProfileUpdateForm(
        request.POST, request.FILES, instance=request.user.profile
    )
    if request.method == "POST" and user_form.is_valid() and profile_form.is_valid():

        user_form.save() and profile_form.save()
        messages.success(request, f"Your account has been updated!")
        return redirect("profile")
    context = {
        "user_form": user_form,
        "profile_form": profile_form,
        "addresses": addresses,
    }
    return render(request, "users/profile.html", context)
