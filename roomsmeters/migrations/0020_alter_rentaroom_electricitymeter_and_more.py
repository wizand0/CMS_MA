# Generated by Django 4.0.6 on 2022-07-22 17:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('roomsmeters', '0019_remove_electricitydate_difference_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rentaroom',
            name='electricitymeter',
            field=models.OneToOneField(default=0, on_delete=django.db.models.deletion.CASCADE, to='roomsmeters.electricitymeter'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='rentaroom',
            name='lessor',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='roomsmeters.lessor'),
        ),
        migrations.AlterField(
            model_name='rentaroom',
            name='room',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='roomsmeters.room'),
        ),
        migrations.AlterField(
            model_name='rentaroom',
            name='watermeter',
            field=models.OneToOneField(default=0, on_delete=django.db.models.deletion.CASCADE, to='roomsmeters.watermeter'),
            preserve_default=False,
        ),
    ]