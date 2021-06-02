from cuid import cuid
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from users.forms import ProfileUpdateForm, UserRegisterForm, UserUpdateForm
from users.models import Profile

address_switcher = {
     "MAIL":"Mailing",
"RESD":"Residential",
"BUSN":"Business",
}
def homepage(request):
    return render(request, "users/home.html")


def about(request):
    return render(request, "users/about.html")


def registration(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(
                request, f"Your account has been created! You are now able to log in"
            )
            return redirect("login")
    else:
        form = UserRegisterForm()
    return render(request, "users/register.html", {"form": form})


@login_required
def profile(request):
    addr = Profile.objects.get(user=request.user).addresses.all()
    addresses = [
        {
            "idempotent_key":address.idempotent_key,
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
