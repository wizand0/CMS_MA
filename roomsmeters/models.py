from django.db import models


class Watermeter(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название")
    serialnumber = models.CharField(unique=True, max_length=30, primary_key=True, null=False, blank=False,
                                    verbose_name="Серийный номер")
    verificationdate = models.DateField(blank=True, null=True, default="", verbose_name="Дата поверки")
    #startdate = models.DateField(verbose_name="Дата установки")

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-serialnumber']
        verbose_name_plural = 'Счетчики воды'
        verbose_name = 'Счетчик воды'


class Electricitymeter(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название")
    serialnumber = models.CharField(unique=True, max_length=30, primary_key=True, null=False, blank=False,
                                    verbose_name="Серийный номер")
    #startdate = models.DateField(verbose_name="Дата установки")
    verificationdate = models.DateField(blank=True, verbose_name="Дата поверки")
    ratio_transform = models.PositiveSmallIntegerField(null=False, blank=False, default=1,
                                                       verbose_name="Коэффициент трансформации")
    ratio_loss = models.FloatField(null=False, blank=False, default=1.2,
                                                  verbose_name="Коэффициент потерь")

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-serialnumber']
        verbose_name_plural = 'Счетчики электроэнергии'
        verbose_name = 'Счетчик электроэнергии'


class Renter(models.Model):
    name = models.CharField(unique=True, max_length=100, verbose_name="Название арендатора")

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-name']
        verbose_name_plural = 'Арендаторы'
        verbose_name = 'Арендатор'


class Lessor(models.Model):
    name = models.CharField(unique=True, max_length=100, verbose_name="Название Арендодателя")

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-name']
        verbose_name_plural = 'Арендодатели'
        verbose_name = 'Арендодатель'


class Room(models.Model):
    name = models.CharField(unique=True, max_length=100, verbose_name="Номер(название) помещения")
    roomsquare = models.PositiveSmallIntegerField(blank=False, verbose_name="Площадь помещения")
    building = models.CharField(max_length=10, verbose_name="Корпус")
    floor = models.CharField(max_length=10, verbose_name="Этаж")

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-name']
        verbose_name_plural = 'Помещения'
        verbose_name = 'Помещение'


class Spotelectr(models.Model):
    name = models.CharField(max_length=2, unique=True, verbose_name="Название участка")

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-name']
        verbose_name_plural = 'Участки по электроэнергии'
        verbose_name = 'Участок по электроэнергии'


class Spotwater(models.Model):
    name = models.CharField(max_length=2, unique=True, verbose_name="Название участка")

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-name']
        verbose_name_plural = 'Участки по воде'
        verbose_name = 'Участок по воде'


class Rentaroom(models.Model):
    room = models.ForeignKey(Room, verbose_name="Помещение, которое снял арендатор", on_delete=models.CASCADE)
    renter = models.ForeignKey(Renter, verbose_name="Название арендатора", on_delete=models.CASCADE)
    iswater = models.BooleanField(blank=False, default=False, verbose_name="Есть вода?")
    watermeter = models.ForeignKey(Watermeter, blank=True, null=True, on_delete=models.CASCADE,
                                   verbose_name="Счетчик воды")
    tarifofwater = models.FloatField(blank=False, null=False, default=9, verbose_name="Тариф вода")
    iselectricity = models.BooleanField(blank=False, default=True, verbose_name="Есть электроэнергия?")
    electricitymeter = models.ForeignKey(Electricitymeter, blank=True, null=True, on_delete=models.CASCADE,
                                         verbose_name="Счетчик электроэнергии")
    tarifofelectricity = models.FloatField(blank=False, null=False, default=11.8,
                                                          verbose_name="Тариф за электроэнергию")
    datestart = models.DateField(verbose_name="Дата начала аренды или изменение условий")
    dateend = models.DateField(verbose_name="Дата окончания аренды", null=True, blank=True)
    spotelectr = models.ForeignKey(Spotelectr, default="", verbose_name="Название участка для Электроэнергии",
                                   on_delete=models.CASCADE)
    spotwater = models.ForeignKey(Spotwater, default="", verbose_name="Название участка для воды", on_delete=models.CASCADE)
    lessor = models.ForeignKey(Lessor, default="", verbose_name="Название арендодателя", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.room} - {self.renter} - {self.lessor}"

    class Meta:
        ordering = ['-room']
        verbose_name_plural = 'Какие помещения арендованы и кем'
        verbose_name = 'Какое помещение арендовано и кем'


class Waterdate(models.Model):
    serialnumber = models.ForeignKey(Watermeter, blank=True, null=True, on_delete=models.CASCADE,
                                     verbose_name="Серийный номер")
    datedata = models.DateField(null=False, blank=False, verbose_name="Дата снятия показаний")
    consumption = models.PositiveSmallIntegerField(blank=False, verbose_name="Текущее показание")
    difference = models.PositiveIntegerField(blank=False, default=0, verbose_name="Разность")
    suminrubles = models.FloatField(blank=False, default=0, verbose_name="Сумма реализации")

    def __str__(self):
        return f"{self.datedata} - {self.serialnumber} - {self.consumption}"

    class Meta:
        ordering = ['-serialnumber']
        verbose_name_plural = 'Показания счетчиков воды'
        verbose_name = 'Показание счетчика вода'


class Electricitydate(models.Model):
    serialnumber = models.ForeignKey(Electricitymeter, blank=True, null=True, on_delete=models.CASCADE,
                                     verbose_name="Серийный номер")
    datedata = models.DateField(null=False, blank=False, verbose_name="Дата снятия показаний")
    consumption = models.PositiveIntegerField(blank=False, verbose_name="Текущие показание")
    difference = models.PositiveIntegerField(blank=False, default=0, verbose_name="Разность")
    suminrubles = models.FloatField(blank=False, default=0, verbose_name="Сумма реализации")

    def __str__(self):
        return f"{self.datedata} - {self.serialnumber} - {self.consumption}"

    class Meta:
        ordering = ['-datedata']
        verbose_name_plural = 'Показания счетчиков электроэнергии'
        verbose_name = 'Показание счетчика электроэнергии'
