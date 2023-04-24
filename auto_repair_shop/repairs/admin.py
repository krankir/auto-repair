from django.contrib import admin

from repairs.models import Repair


@admin.register(Repair)
class RepairAdmin(admin.ModelAdmin):
    ...

