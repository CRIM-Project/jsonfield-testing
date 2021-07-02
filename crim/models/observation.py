from django.db import models
from django.db.models import JSONField

# Create your models here.
class CRIMObservation(models.Model):
    class Meta:
        app_label = 'crim'
        verbose_name = 'Observation'
        verbose_name_plural = 'Observations'


    # This is trial for JSONField application
    observer = models.CharField(max_length=128, blank=True)
    musical_type = models.CharField(max_length=128, blank=True)
    details = JSONField(null=True) 

    def __str__(self):
        return self.musical_type

    