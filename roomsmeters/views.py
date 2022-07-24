from datetime import timedelta

from django.conf import settings as conf_settings
from django.shortcuts import render

from .forms import WatermeterForm, RentaroomForm, ElectricitymeterForm, WaterdateForm, ElectricitydateForm, MyForm
from .models import Electricitymeter, Rentaroom, Room, Watermeter, Electricitydate


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
            startdataperiod = form['startdataperiod']
            enddataperiod = form['enddataperiod']

            pk = form['lessor']

            pkid = pk.id

            obj = Rentaroom.objects.all().filter(lessor_id=pkid)

            startdate = startdataperiod - timedelta(days=3)
            enddate = startdataperiod + timedelta(days=3)

            startconsumption = Electricitydate.objects.filter(datedata__range=[startdate, enddate])

            sumofkilowatt = 25
            context = {
                'obj': obj,
                'startdataperiod': startdataperiod,
                'enddataperiod': enddataperiod,
                'sumofkilowatt': sumofkilowatt,
                'pk': pk,

            }

        return render(request, 'roomsmeters/outputmetersdata.htm', context)
    else:
        form = MyForm()

    return render(request, 'roomsmeters/outputmetersdata.htm', {'form': form})
