from django.db import models
from django.db.models import JSONField

# Create your models here.
class CRIMRelationship(models.Model):
    class Meta:
        app_label = 'crim'
        verbose_name = 'Relationship'
        verbose_name_plural = 'Relationships'


    # This is trial for JSONField application  
    model_observation = models.ForeignKey(
        'CRIMObservation',
        on_delete=models.CASCADE,
        db_index=True,
        related_name='observations_as_model',
        null=True
    )

    derivative_observation = models.ForeignKey(
        'CRIMObservation',
        on_delete=models.CASCADE,
        db_index=True,
        related_name='observations_as_derivative',
        null=True
    )
    
    musical_type = models.CharField(max_length=128, blank=True)
    relationship_type = models.CharField(max_length=128, blank=True)
    details = JSONField(null=True) 

    def __str__(self):
        return self.relationship_type
