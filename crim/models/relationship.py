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
    
    observer = models.CharField(max_length=128, blank=True)
    musical_type = models.CharField(max_length=128, blank=True)
    relationship_type = models.CharField(max_length=128, blank=True)
    details = JSONField(null=True) 

    def __str__(self):
        return self.relationship_type


    #def save(self, *args, **kwargs):

        # For the musical type field, check if both observations use the same
        # musical type; otherwise, use whichever has a musical type if one of
        # them doesn't (e.g. omission), or include them both.
    #    if self.model_observation['musical_type'] and self.derivative_observation['musical_type']:
    #        mt1 = self.model_observation['musical_type']
    #        self.musical_type = 
    #    elif self.model_observation.musical_type:
    #        self.musical_type = self.model_observation.musical_type
    #    elif self.derivative_observation.musical_type:
    #        self.musical_type = self.derivative_observation.musical_type
    #    else:
    #        self.musical_type = '{0}; {1}'.format(
    #            self.model_observation.musical_type,
    #            self.derivative_observation.musical_type,
    #        )

        # Save observations, thus caching them
    #    self.model_observation.save()
    #    self.derivative_observation.save()
        # Finalize changes
    #    super().save()