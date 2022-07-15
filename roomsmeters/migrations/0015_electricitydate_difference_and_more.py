# Generated by Django 4.0.6 on 2022-07-15 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('roomsmeters', '0014_alter_rentaroom_dateend'),
    ]

    operations = [
        migrations.AddField(
            model_name='electricitydate',
            name='difference',
            field=models.PositiveIntegerField(default=0, verbose_name='Разность'),
        ),
        migrations.AddField(
            model_name='electricitydate',
            name='suminrubles',
            field=models.FloatField(default=0, verbose_name='Сумма реализации'),
        ),
        migrations.AddField(
            model_name='waterdate',
            name='difference',
            field=models.PositiveIntegerField(default=0, verbose_name='Разность'),
        ),
        migrations.AddField(
            model_name='waterdate',
            name='suminrubles',
            field=models.FloatField(default=0, verbose_name='Сумма реализации'),
        ),
    ]
