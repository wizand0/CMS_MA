from django.shortcuts import render
from django.conf import settings as conf_settings
from .models import Electricitymeter, Rentaroom, Room, Watermeter



def allmeters_list(request):
    template_name = 'roomsmeters/roomsandmeters.html'
    Electricitymeter_objects = Electricitymeter.objects.all()
    Electricitymeter_number = Electricitymeter_objects.count()
    Watermeter_objects = Watermeter.objects.all()
    Watermeter_number = Watermeter_objects.count()
    Rentaroom_objects = Rentaroom.objects.all()
    Room_objects = Room.objects.all()
    app_version = conf_settings.APP_VERSION

    context = {
        'Electricitymeter_objects': Electricitymeter_objects,
        'Watermeter_objects': Watermeter_objects,
        'Rentaroom_objects': Rentaroom_objects,
        'Room_objects': Room_objects,
        'Electricitymeter_number': Electricitymeter_number,
        'Watermeter_number': Watermeter_number,
        'app_version': app_version,
    }
    return render(request, template_name, context)
