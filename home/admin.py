from django.contrib import admin

from .models import Group, Event


admin.site.register([Group, Event])
