from django.db import models


class Watermeter(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название")
    serialnumber = models.CharField(max_length=30, primary_key=True, null=False, blank=False, verbose_name="Серийный номер")
    verificationdate = models.DateField(blank=True, verbose_name="Дата поверки")

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-serialnumber']
        verbose_name_plural = 'Счетчики воды'
        verbose_name = 'Счетчик воды'


class Electricitymeter(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название")
    serialnumber = models.CharField(max_length=30, primary_key=True, null=False, blank=False, verbose_name="Серийный номер")
    verificationdate = models.DateField(blank=True, verbose_name="Дата поверки")
    ratio_transform = models.PositiveSmallIntegerField(null=False, blank=False, default=1,
                                                       verbose_name="Коэффициент трансформации")
    ratio_loss = models.PositiveSmallIntegerField(null=False, blank=False, default=1.2,
                                                  verbose_name="Коэффициент потерь")



    def __str__(self):
        return self.name


    class Meta:
        ordering = ['-serialnumber']
        verbose_name_plural = 'Счетчики электроэнергии'
        verbose_name = 'Счетчик электроэнергии'


class Renter(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название арендатора")
    iswater = models.BooleanField(blank=False, default=False, verbose_name="Есть вода?")
    watermeter = models.ForeignKey(Watermeter, blank=True, null=True, on_delete=models.CASCADE,
                                   verbose_name="Счетчик воды")
    tarifofwater = models.PositiveSmallIntegerField(blank=False, null=False, default=9, verbose_name="Тариф вода")
    iselectricity = models.BooleanField(blank=False, default=True, verbose_name="Есть электроэнергия?")
    electricitymeter = models.ForeignKey(Electricitymeter, blank=True, null=True, on_delete=models.CASCADE,
                                         verbose_name="Счетчик электроэнергии")
    tarifofelectricity = models.PositiveSmallIntegerField(blank=False, null=False, default=11.8,
                                                          verbose_name="Тариф за электроэнергию")

    def __str__(self):
        return self.name


    class Meta:
        ordering = ['-name']
        verbose_name_plural = 'Арендаторы'
        verbose_name = 'Арендатор'


class Room(models.Model):
    name = models.CharField(max_length=100, verbose_name="Номер(название) помещения")
    roomsquare = models.PositiveSmallIntegerField(blank=False, verbose_name="Площадь помещения")
    building = models.CharField(max_length=10, verbose_name="Корпус")
    floor = models.CharField(max_length=10, verbose_name="Этаж")
    renter = models.ForeignKey(Renter, blank=True, null=True, on_delete=models.CASCADE, verbose_name="Арендатор")

    def __str__(self):
        return self.name


    class Meta:
        ordering = ['-name']
        verbose_name_plural = 'Помещения'
        verbose_name = 'Помещение'


class Waterdate(models.Model):
    serialnumber = models.ForeignKey(Watermeter, blank=True, null=True, on_delete=models.CASCADE,
                                     verbose_name="Серийный номер")
    datedata = models.DateField(auto_now=True, null=False, blank=False, verbose_name="Дата снятия показаний")
    consumption = models.PositiveSmallIntegerField(blank=False, verbose_name="Текущее показание")

    def __str__(self):
        return self.serialnumber


    class Meta:
        ordering = ['-serialnumber']
        verbose_name_plural = 'Показания счетчиков воды'
        verbose_name = 'Показание счетчика вода'


class Electricitydate(models.Model):
    serialnumber = models.ForeignKey(Electricitymeter, blank=True, null=True, on_delete=models.CASCADE,
                                     verbose_name="Серийный номер")
    datedata = models.DateField(null=False, blank=False, verbose_name="Дата снятия показаний")
    consumption = models.PositiveSmallIntegerField(blank=False, verbose_name="Текущие показание")

    def __str__(self):
        return self.serialnumber


    class Meta:
        ordering = ['-serialnumber']
        verbose_name_plural = 'Показания счетчиков электроэнергии'
        verbose_name = 'Показание счетчика электроэнергии'




