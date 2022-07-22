import datetime

from django.conf import settings as conf_settings
from .models import Electricitymeter, Rentaroom, Room, Watermeter, Lessor, Waterdate
from .forms import WatermeterForm, RentaroomForm, ElectricitymeterForm, WaterdateForm, ElectricitydateForm, MyForm

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


def electricitymeter_create(request):
    if request.method == "POST":
        form = ElectricitymeterForm(request.POST)

        if form.is_valid():
            electricitymeter = form.save(commit=False)
            electricitymeter.name = electricitymeter.serialnumber
            electricitymeter.save()
            return render(request, 'roomsmeters/add_electricitymeter.htm', {'form': form})
            # return redirect('electricitymeter_detail', pk=electricitymeter.pk)
    else:
        form = ElectricitymeterForm()
    return render(request, 'roomsmeters/add_electricitymeter.htm', {'form': form})


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


def add_waterdata(request):
    if request.method == "POST":
        form = WaterdateForm(request.POST)
        if form.is_valid():
            waterdate = form.save(commit=False)

            waterdate.save()
            return render(request, 'roomsmeters/add_waterdata.htm', {'form': form})
    else:
        form = WaterdateForm()

    return render(request, 'roomsmeters/add_waterdata.htm', {'form': form})


def add_electricitydate(request):
    if request.method == "POST":
        form = ElectricitydateForm(request.POST)
        if form.is_valid():
            electricitydate = form.save(commit=False)

            electricitydate.save()
            return render(request, 'roomsmeters/add_electricitydate.htm', {'form': form})
    else:
        form = ElectricitydateForm()

    return render(request, 'roomsmeters/add_electricitydate.htm', {'form': form})


def outputmetersdata(request):
    form = MyForm()
    if request.method == 'POST':
        form = MyForm(request.POST)

        if form.is_valid():
            form = form.cleaned_data
            # now in the object cd, you have the form as a dictionary.
            pk = form['lessor']

            pkid = pk.id

            obj = Rentaroom.objects.all().filter(lessor_id=pkid)

            # room = obj.room
            #
            # electricitymeter
            # electricitymeter_id = obj.electricitymeter_id
            # id
            # iselectricity
            # isfree
            # iswater
            # lessor
            # lessor_id
            # renter
            # renter_id
            # room
            # room_id
            # spotelectr
            # spotelectr_id
            # spotwater
            # spotwater_id
            # tarifofelectricity
            # tarifofwater
            # watermeter
            #
            # Waterdate.electricitymeter_id
            # objel = Waterdate.objects.get(electricitymeter_id=electricitymeter_id)
            # datedata = objel.datedata
            # consumption = objel.consumption
            # difference = objel.difference
            # suminrubles = objel.suminrubles
            context = {
                'obj': obj,
                # 'electricitymeter_id': electricitymeter_id,
            }

        return render(request, 'roomsmeters/outputmetersdata.htm',  context)
    else:
        form = MyForm()

    return render(request, 'roomsmeters/outputmetersdata.htm', {'form': form})

    # blah blah encode parameters for a url blah blah
    # and make another post request
    # edit : added ": "  after    if request.method=='POST'


