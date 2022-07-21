import datetime

from django import forms
from django.conf import settings

from .models import Watermeter, Electricitymeter, Rentaroom

from django.db import models
from django.forms import ModelForm

class WatermeterForm(forms.ModelForm):
    verificationdate = forms.DateField(required=False, input_formats=settings.DATE_INPUT_FORMATS)

    class Meta:
        model = Watermeter
        fields = ('serialnumber', 'verificationdate')


class ElectricitymeterForm(forms.ModelForm):
    class Meta:
        serialnumber = Electricitymeter
        fields = ('serialnumber', 'verificationdate', 'ratio_transform', 'ratio_loss')


class RentaroomForm(forms.ModelForm):
    tempstartdate = datetime.date.today().strftime('%d.%m.%Y')
    datestart = forms.DateField(required=True, initial=tempstartdate,
                                input_formats=settings.DATE_INPUT_FORMATS)
    dateend = forms.DateField(required=False,
                                input_formats=settings.DATE_INPUT_FORMATS)
    class Meta:
        model = Rentaroom
        fields = ('room', 'renter', 'iswater', 'watermeter', 'tarifofwater', 'iselectricity',
                  'electricitymeter', 'tarifofelectricity', 'datestart', 'dateend',
                  'spotelectr', 'spotwater', 'lessor')
