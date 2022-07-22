# Generated by Django 4.0.6 on 2022-07-22 17:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('roomsmeters', '0020_alter_rentaroom_electricitymeter_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rentaroom',
            name='lessor',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='roomsmeters.lessor', verbose_name='Арендодатель'),
        ),
    ]
