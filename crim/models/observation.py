from django.db import models
from django.db.models import JSONField
from crim.models.definition import CRIMDefinition
import json

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
    
    definition = models.ForeignKey(
        CRIMDefinition,
        on_delete=models.CASCADE,
        db_index=True,
        related_name='definition',
        null=True
    )

    def __str__(self):
        return str(self.pk)

    def save(self, *args, **kwargs):
        mtypename = str(self.musical_type).lower()
        allowed_types = list(self.definition.observation_definition.keys())

        if mtypename in allowed_types:
            valid_sub = False
            allowed_subtypes = sorted(list(self.definition.observation_definition[mtypename]))
            string_details = json.dumps(self.details)
            sub_dict = json.loads(string_details)

            curr_subtypes = sorted(list(sub_dict.keys()))
            curr_subtypes_lower = [e.lower() for e in curr_subtypes]

            if allowed_subtypes == []:
                valid_sub = True
            elif curr_subtypes_lower == allowed_subtypes:
                valid_sub = True
        
            if valid_sub:
                print('validated. saving obs...')
                self.definition.save()
                super(CRIMObservation, self).save(*args, **kwargs)
                print('obs saved')
            else:
                print('subtypes not valid')
        else:
            print('Error saving, mtypename not in allowed musical types')

