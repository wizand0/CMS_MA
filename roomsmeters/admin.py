from django.contrib import admin
from . import models


@admin.register(models.Watermeter)
class WatermeterAdmin(admin.ModelAdmin):
    list_display = ['name', 'serialnumber', 'verificationdate']


@admin.register(models.Electricitymeter)
class ElectricitymeterAdmin(admin.ModelAdmin):
    list_display = ['name', 'serialnumber', 'ratio_transform', 'ratio_loss', 'verificationdate']


@admin.register(models.Renter)
class RenterAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ['name', 'building', 'floor', 'roomsquare']


@admin.register(models.Waterdate)
class WaterdateAdmin(admin.ModelAdmin):
    list_display = ['serialnumber', 'datedata', 'consumption', 'difference', 'suminrubles']
    list_filter = ['serialnumber', 'datedata']


@admin.register(models.Electricitydate)
class ElectricitydateAdmin(admin.ModelAdmin):
    list_display = ['serialnumber', 'datedata', 'consumption', 'difference', 'suminrubles']
    list_filter = ['serialnumber', 'datedata']


@admin.register(models.Rentaroom)
class RentaroomAdmin(admin.ModelAdmin):
    list_display = ['room', 'renter', 'watermeter', 'tarifofwater', 'electricitymeter',
                    'tarifofelectricity', 'lessor']


@admin.register(models.Lessor)
class LessorAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Spotwater)
class SpotwaterAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Spotelectr)
class SpotelectrAdmin(admin.ModelAdmin):
    pass
