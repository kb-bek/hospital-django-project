from django.contrib import admin
from .models import *

admin.site.register(Hospital)
admin.site.register(MainDoctor)
admin.site.register(AttendingDoctor)
admin.site.register(Nurse)
admin.site.register(Patient)