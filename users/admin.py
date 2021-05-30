from django.contrib.admin import StackedInline, site
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

User = get_user_model()


# class EmployeeInline(StackedInline):
#     model = Employee
#     can_delete = False
#     verbose_name_plural = 'employee'

# # Define a new User admin
# class UserAdmin(BaseUserAdmin):
#     inlines = (EmployeeInline,)

# # Re-register UserAdmin
# site.unregister(User)
# site.register(User, UserAdmin)
