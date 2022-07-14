from django.contrib import admin
from . import models


@admin.register(models.Watermeter)
class WatermeterAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Electricitymeter)
class ElectricitymeterAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Renter)
class RenterAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Waterdate)
class WaterdateAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Electricitydate)
class ElectricitydateAdmin(admin.ModelAdmin):
    pass
