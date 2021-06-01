from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from users.forms import ProfileUpdateForm, UserRegisterForm, UserUpdateForm


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
    from django.conf import settings

    user_form = UserUpdateForm(request.POST, instance=request.user)
    profile_form = ProfileUpdateForm(
        request.POST, request.FILES, instance=request.user.profile
    )
    if request.method == "POST" and user_form.is_valid() and profile_form.is_valid():
        user_form.save() and profile_form.save()
        messages.success(request, f"Your account has been updated!")
        return redirect("profile")
    context = {"user_form": user_form, "profile_form": profile_form}
    print(settings.MEDIA_URL)
    return render(request, "users/profile.html", context)
