# Generated by Django 4.0.6 on 2022-07-14 19:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('roomsmeters', '0007_alter_spotelectr_options_alter_spotwater_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='electricitymeter',
            options={'ordering': ['-serialnumberel'], 'verbose_name': 'Счетчик электроэнергии', 'verbose_name_plural': 'Счетчики электроэнергии'},
        ),
        migrations.RenameField(
            model_name='electricitymeter',
            old_name='name',
            new_name='nameel',
        ),
        migrations.RenameField(
            model_name='electricitymeter',
            old_name='ratio_loss',
            new_name='ratio_lossel',
        ),
        migrations.RenameField(
            model_name='electricitymeter',
            old_name='ratio_transform',
            new_name='ratio_transformel',
        ),
        migrations.RenameField(
            model_name='electricitymeter',
            old_name='serialnumber',
            new_name='serialnumberel',
        ),
        migrations.RenameField(
            model_name='electricitymeter',
            old_name='verificationdate',
            new_name='verificationdateel',
        ),
    ]
