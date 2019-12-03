from django.contrib import admin
from .models import Service, Invoice

admin.site.register(Service)
admin.site.register(Invoice)