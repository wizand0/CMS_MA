from django.shortcuts import render
from .models import Electricitymeter, Rentaroom

def electricitymeters_list(request):
    template_name = 'roomsmeters/electricitymeters.html'
    Electricitymeter_objects = Electricitymeter.objects.all()
    Electricitymeter_number = Electricitymeter_objects.count()
    Rentaroom_objects = Rentaroom.objects.all()
    context = {
        'Electricitymeter_objects': Electricitymeter_objects,
        'Rentaroom_objects' : Rentaroom_objects,
        'Electricitymeter_number': Electricitymeter_number,
    }
    return render(request, template_name, context)