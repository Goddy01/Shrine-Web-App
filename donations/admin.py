from django.contrib import admin
from .models import Donation, Donated
# Register your models here.
admin.site.register(Donation)
admin.site.register(Donated)