from django.contrib import admin
from .models import Pet, Shelter, Application

# Register your models here.
admin.site.register(Pet)
admin.site.register(Shelter)
admin.site.register(Application)