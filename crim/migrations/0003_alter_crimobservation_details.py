# Generated by Django 3.2.4 on 2021-06-25 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crim', '0002_remove_crimobservation_observer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crimobservation',
            name='details',
            field=models.JSONField(verbose_name={}),
        ),
    ]
