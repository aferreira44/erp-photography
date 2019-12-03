from django.contrib import admin
from .models import Address

class AddressAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'postal_code', 'city', 'state')

admin.site.register(Address, AddressAdmin)