from django.contrib import admin
from .models import ATMSite, State, City

admin.site.register(ATMSite)
admin.site.register(State)
admin.site.register(City)
