from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Company)
admin.site.register(IncidentType)
admin.site.register(DocumentType)
admin.site.register(Partner)
admin.site.register(PartnerDocument)
admin.site.register(Driver)
admin.site.register(DriverDocument)
admin.site.register(Vehicle)
admin.site.register(VehicleDocument)
admin.site.register(Incident)
admin.site.register(Tip)
admin.site.register(Notification)
