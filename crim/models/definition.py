from django.db import models
from django.db.models import JSONField

# Create your models here.
class CRIMDefinition(models.Model):
    class Meta:
        app_label = 'crim'
        verbose_name = 'Definition'
        verbose_name_plural = 'Definitions'

    observation_definition = JSONField(null=True)
    relationship_definition = JSONField(null=True)
    

    def __str__(self):
        return str(self.pk)