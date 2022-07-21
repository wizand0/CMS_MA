import datetime

from django.conf import settings as conf_settings
from .models import Electricitymeter, Rentaroom, Room, Watermeter
from .forms import WatermeterForm, RentaroomForm

from django.shortcuts import get_object_or_404, redirect, render



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


def watermeter_create(request):
    if request.method == "POST":
        form = WatermeterForm(request.POST)

        if form.is_valid():
            watermeter = form.save(commit=False)
            watermeter.name = watermeter.serialnumber
            watermeter.save()
            return render(request, 'roomsmeters/add_watermeter.htm', {'form': form})
            # return redirect('watermeter_detail', pk=watermeter.pk)
    else:
        form = WatermeterForm()
    return render(request, 'roomsmeters/add_watermeter.htm', {'form': form})

def rentaroom_create(request):
    if request.method == "POST":
        form = RentaroomForm(request.POST)
        if form.is_valid():
            rentaroom = form.save(commit=False)

            rentaroom.save()
            return render(request, 'roomsmeters/add_rentaroom.htm', {'form': form})
    else:
        form = RentaroomForm()

    return render(request, 'roomsmeters/add_rentaroom.htm', {'form': form})
