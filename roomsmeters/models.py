from django.db import models


class Watermeter(models.Model):
    name = models.CharField(max_length=100)
    serialnumber = models.CharField(max_length=30, primary_key=True, null=False, blank=False)
    verificationdate = models.DateField(auto_now=True)

    class Meta:
        ordering = ['-serialnumber']
        verbose_name_plural = 'Счетчики воды'
        verbose_name = 'Счетчик воды'


class Electricitymeter(models.Model):
    name = models.CharField(max_length=100)
    serialnumber = models.CharField(max_length=30, primary_key=True, null=False, blank=False)
    verificationdate = models.DateField(auto_now=True)


    class Meta:
        ordering = ['-serialnumber']
        verbose_name_plural = 'Счетчики электроэнергии'
        verbose_name = 'Счетчик электроэнергии'


class Renter(models.Model):
    name = models.CharField(max_length=100)
    iswater = models.BooleanField(blank=False, default=False)
    watermeter = models.ForeignKey(Watermeter, blank=True, null=True, on_delete=models.CASCADE)
    iselectricity = models.BooleanField(blank=False, default=True)
    electricitymeter = models.ForeignKey(Electricitymeter, blank=True, null=True, on_delete=models.CASCADE)


    class Meta:
        ordering = ['-name']
        verbose_name_plural = 'Арендаторы'
        verbose_name = 'Арендатор'


class Room(models.Model):
    name = models.CharField(max_length=100)
    roomsquare = models.SmallIntegerField(blank=False)
    building = models.CharField(max_length=10)
    floor = models.CharField(max_length=10)
    renter = models.ForeignKey(Renter, blank=True, null=True, on_delete=models.CASCADE)


    class Meta:
        ordering = ['-name']
        verbose_name_plural = 'Помещения'
        verbose_name = 'Помещение'


class Waterdate(models.Model):
    serialnumber = models.ForeignKey(Watermeter, blank=True, null=True, on_delete=models.CASCADE)
    datedata = models.DateField(auto_now=True, null=False, blank=False)
    consumption = models.SmallIntegerField(blank=False)


class Electricitydate(models.Model):
    serialnumber = models.ForeignKey(Electricitymeter, blank=True, null=True, on_delete=models.CASCADE)
    datedata = models.DateField(auto_now=True, null=False, blank=False)
    consumption = models.SmallIntegerField(blank=False)




