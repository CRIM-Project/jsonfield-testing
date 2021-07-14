from django.db import models
from django.db.models import JSONField
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
        'CRIMDefinition',
        on_delete=models.CASCADE,
        db_index=True,
        related_name='definition',
        null=True
    )

    def __str__(self):
        return self.musical_type

    def save(self, *args, **kwargs):
        typename = str(self.musical_type).lower()
        print(typename)
        print('lower success')
        def_dict = self.definition.observation_definition
        typelist = def_dict['musical_types']
        print(def_dict)
        print(typelist)
        if typename in typelist:
            print('passed if 1')
            valid = False
            curr_subtypes = list(self.details.keys()).sort()
            print(curr_subtypes)
            if typename == 'fuga':
                allowed_subtypes = list(def_dict['fg_subtypes']).sort()
                if curr_subtypes == allowed_subtypes:
                    valid = True
            elif typename == 'cadence':
                allowed_subtypes = list(def_dict['cad_subtypes']).sort()
                if curr_subtypes == allowed_subtypes:
                    valid = True
            elif typename == 'homorhythm':
                allowed_subtypes = list(def_dict['hr_subtypes']).sort()
                if curr_subtypes == allowed_subtypes:
                   valid = True
           #add more types later
           
            if valid:
                self.definition.save()
                super(CRIMObservation, self).save(*args, **kwargs)
            else:
                print('subtypes not valid')
        else:
            print('Error saving, typename not in allowed musical types')
