from django.http import HttpResponse
from django.shortcuts import redirect


def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("homepage")
        return view_func(request, *args, **kwargs)

    return wrapper_func


def allowed_users(allowed_roles=()):
    """
    @allowed_users(allowed_roles=('admin', 'supervisor', 'lead'))
    """

    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
            if group in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse("You're not authorized to view this page")

        return wrapper_func

    return decorator


def object_fields(fields=[], model=None):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            _fields = set(fields)

            # _protected_fields = {k:v for k,v in }
            return view_func(request, *args, **kwargs)

        return wrapper_func

    return decorator


#  ryan, interview process
