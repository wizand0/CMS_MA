import datetime

from django import forms
from django.conf import settings
from django.core.exceptions import ValidationError

from .models import Watermeter, Electricitymeter, Rentaroom, Waterdate, Electricitydate, Lessor


class WatermeterForm(forms.ModelForm):
    verificationdate = forms.DateField(required=False, input_formats=settings.DATE_INPUT_FORMATS)

    def clean(self):
        """
        Переписан стандартный метод для исключения дублирования счетчика
        """
        cleaned_data = self.cleaned_data
        serialnumber = cleaned_data.get('serialnumber')

        matching_watermeter = Watermeter.objects.filter(serialnumber=serialnumber)
        if self.instance:
            matching_watermeter = matching_watermeter.exclude(pk=self.instance.pk)
        if matching_watermeter.exists():
            msg = u"Счетчик с серийным номером: %s уже внесен в БД." % serialnumber
            raise ValidationError(msg)
        else:
            return self.cleaned_data

    class Meta:
        model = Watermeter
        fields = ('serialnumber', 'verificationdate')


class ElectricitymeterForm(forms.ModelForm):
    verificationdate = forms.DateField(required=False, input_formats=settings.DATE_INPUT_FORMATS)

    def clean(self):
        """
        Переписан стандартный метод для исключения дублирования счетчика
        """
        cleaned_data = self.cleaned_data
        serialnumber = cleaned_data.get('serialnumber')

        matching_electricitymeter = Electricitymeter.objects.filter(serialnumber=serialnumber)
        if self.instance:
            matching_electricitymeter = matching_electricitymeter.exclude(pk=self.instance.pk)
        if matching_electricitymeter.exists():
            msg = u"Счетчик с серийным номером: %s уже внесен в БД." % serialnumber
            raise ValidationError(msg)
        else:
            return self.cleaned_data

    class Meta:
        model = Electricitymeter
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

    def clean(self):
        """
        Переписан стандартный метод для исключения дублирования счетчика
        """
        cleaned_data = self.cleaned_data
        room = cleaned_data.get('room')

        matching_room = Rentaroom.objects.filter(room=room)
        if self.instance:
            matching_room = matching_room.exclude(pk=self.instance.pk)
        if matching_room.exists():
            msg = u"Помещение с номером: %s уже снято арендатором и внесено в БД." % room
            raise ValidationError(msg)
        else:
            return self.cleaned_data


class WaterdateForm(forms.ModelForm):
    tempstartdate = datetime.date.today().strftime('%Y-%m-%d')

    cur_ds = datetime.datetime.strptime(tempstartdate, '%Y-%m-%d')
    next_month = datetime.datetime(year=cur_ds.year, month=cur_ds.month + 1, day=1)
    # Reduce 12 to 1, 0 and all other #s to 0, #
    extrayear, month = divmod(cur_ds.month, 12)
    # Add 1 or 0 to existing year, add one to month (which was reduced to 0-11)
    next_month = datetime.datetime(year=cur_ds.year + extrayear, month=month + 1, day=1)
    next_month_newformat = next_month.strftime('%d.%m.%Y')
    next_month_newformat = next_month - datetime.timedelta(days=1)

    datedata = forms.DateField(required=True, initial=next_month_newformat, input_formats=settings.DATE_INPUT_FORMATS)

    class Meta:
        model = Waterdate
        fields = ('serialnumber', 'datedata', 'consumption')


class ElectricitydateForm(forms.ModelForm):
    tempstartdate = datetime.date.today().strftime('%Y-%m-%d')

    cur_ds = datetime.datetime.strptime(tempstartdate, '%Y-%m-%d')
    next_month = datetime.datetime(year=cur_ds.year, month=cur_ds.month + 1, day=1)
    # Reduce 12 to 1, 0 and all other #s to 0, #
    extrayear, month = divmod(cur_ds.month, 12)
    # Add 1 or 0 to existing year, add one to month (which was reduced to 0-11)
    next_month = datetime.datetime(year=cur_ds.year + extrayear, month=month + 1, day=1)
    next_month_newformat = next_month.strftime('%d.%m.%Y')
    next_month_newformat = next_month - datetime.timedelta(days=1)

    datedata = forms.DateField(required=True, initial=next_month_newformat, input_formats=settings.DATE_INPUT_FORMATS)

    class Meta:
        model = Electricitydate
        fields = ('serialnumber', 'datedata', 'consumption')


class MyForm(forms.Form):  # Note that it is not inheriting from forms.ModelForm
    startdataperiod = forms.DateField(required=True, input_formats=settings.DATE_INPUT_FORMATS)
    enddataperiod = forms.DateField(required=True, input_formats=settings.DATE_INPUT_FORMATS)

    lessor = forms.ModelChoiceField(queryset=Lessor.objects.all())

    GEEKS_CHOICES = (

        ("1", "One"),

        ("2", "Two"),

        ("3", "Three"),

        ("4", "Four"),

        ("5", "Five"),

    )
    # lessor = forms.ChoiceField(choices=GEEKS_CHOICES)



    # All my attributes here
