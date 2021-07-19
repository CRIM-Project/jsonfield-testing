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

    definition = models.ForeignKey(
        'CRIMDefinition',
        on_delete=models.CASCADE,
        db_index=True,
        related_name='definition_for_relationship',
        null=True
    )
    
    observer = models.CharField(max_length=128, blank=True)
    musical_type = models.CharField(max_length=128, blank=True)
    relationship_type = models.CharField(max_length=128, blank=True)
    details = JSONField(null=True) 

    def __str__(self):
        return str(self.pk)

    def save(self, *args, **kwargs):

        # For the musical type field, check if both observations use the same
        # musical type; otherwise, use whichever has a musical type if one of
        # them doesn't (e.g. omission), or include them both.
        if self.model_observation.musical_type and self.derivative_observation.musical_type:
            mt1 = self.model_observation.musical_type
            mt2 = self.derivative_observation.musical_type
            self.musical_type = mt1 + ', ' + mt2
        elif self.model_observation.musical_type:
            self.musical_type = self.model_observation.musical_type
        elif self.derivative_observation.musical_type:
            self.musical_type = self.derivative_observation.musical_type

        #Validation for model instance pre-save
        rtypename = str(self.relationship_type).lower()
        def_dict = self.definition.relationship_definition
        if rtypename in def_dict:
            valid_sub = False
            allowed_subtypes = sorted(list(def_dict[rtypename]))
            curr_subtypes = sorted(list(self.details.keys()))
            if allowed_subtypes == []:
                valid_sub = True
            elif curr_subtypes == allowed_subtypes:
                valid_sub = True
        
            if valid_sub:
                print('validated. saving rela...')
                self.model_observation.save()
                self.derivative_observation.save()
                self.definition.save()
                super(CRIMRelationship, self).save(*args, **kwargs)
            else:
                print('subtypes not valid')
        else:
            print('Error saving, rtypename not in allowed relationship types')

