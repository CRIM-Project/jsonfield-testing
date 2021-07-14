# Generated by Django 3.2.4 on 2021-07-14 21:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crim', '0009_crimdefinition'),
    ]

    operations = [
        migrations.AddField(
            model_name='crimobservation',
            name='definition',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='definition', to='crim.crimdefinition'),
        ),
    ]
