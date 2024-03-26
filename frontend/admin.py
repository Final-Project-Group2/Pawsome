from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin
from .forms import CustomerUserForm  , AdminForm
from .models import CustomerUser , Pet

#admin.site.register(CustomerUser)


class CustomerAdmin(UserAdmin):
      add_form = CustomerUserForm
      form = AdminForm
      model = CustomerUser
      list_display = [
            "username",
            "email",
            "is_staff",
      ]
      fieldsets = UserAdmin.fieldsets + ((None, {"fields":("username") }),)
      add_fieldsets = UserAdmin.add_fieldsets + ((None, {"fields": ("username",)}),)
#admin.site.register([],admin_class= CustomerAdmin)
#admin.site.register(Pet)


