from django.db import models
from django.db.models import JSONField
from crim.models.definition import CRIMDefinition
from crim.models.observation import CRIMObservation
import json

# Create your models here.
class CRIMRelationship(models.Model):
    class Meta:
        app_label = 'crim'
        verbose_name = 'Relationship'
        verbose_name_plural = 'Relationships'


    # This is trial for JSONField application  
    model_observation = models.ForeignKey(
        CRIMObservation,
        on_delete=models.CASCADE,
        db_index=True,
        related_name='observations_as_model',
        null=True
    )

    derivative_observation = models.ForeignKey(
        CRIMObservation,
        on_delete=models.CASCADE,
        db_index=True,
        related_name='observations_as_derivative',
        null=True
    )

    definition = models.ForeignKey(
        CRIMDefinition,
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
            if not mt1 == mt2:
                self.musical_type = mt1 + ', ' + mt2
            else:
                self.musical_type = mt1
        elif self.model_observation.musical_type:
            self.musical_type = self.model_observation.musical_type
        elif self.derivative_observation.musical_type:
            self.musical_type = self.derivative_observation.musical_type

        #Validation for model instance pre-save
        rtypename = str(self.relationship_type).lower()
        allowed_types = list(self.definition.relationship_definition.keys())
       
        if rtypename in allowed_types:
            valid_sub = False
            allowed_subtypes = sorted(list(self.definition.relationship_definition[rtypename]))
            string_details = json.dumps(self.details)
            sub_dict = json.loads(string_details)
            
            curr_subtypes = sorted(list(sub_dict.keys()))
            curr_subtypes_lower = [e.lower() for e in curr_subtypes]
            
            if allowed_subtypes == []:
                valid_sub = True
            elif curr_subtypes_lower == allowed_subtypes:
                valid_sub = True
        
            if valid_sub:
                print('validated. saving rela...')
                self.model_observation.save()
                print('model observation saved.')
                self.derivative_observation.save()
                print('derivative observation saved.')
                self.definition.save()
                super(CRIMRelationship, self).save(*args, **kwargs)
                print('rela saved')
            else:
                print('subtypes not valid')
        else:
            print('Error saving, rtypename not in allowed relationship types')

