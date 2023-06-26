from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(DriverExpense)
admin.site.register(VehicleExpense)
admin.site.register(GlobalExpense)
admin.site.register(Payment)
admin.site.register(Payout)
admin.site.register(Ledger)
