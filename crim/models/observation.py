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
    
    definition = models.ForeignKey(
        'CRIMDefinition',
        on_delete=models.CASCADE,
        db_index=True,
        related_name='definition',
        null=True
    )

    def __str__(self):
        return self.musical_type

    #def save(self, *args, **kwargs):
    #    typename = str(self.musical_type).lower()
    #    if typename in list(self.definition.observation_definition.musical_types):
    #       valid = False
    #       def_dict = json.loads(self.definition.observation_definition) 
    #       curr_subtypes = list(self.details.keys()).sort()
    #       if typename == 'fuga':
    #           allowed_subtypes = list(def_dict['fg_subtypes']).sort()
    #           if curr_subtypes == allowed_subtypes:
    #               valid = True
    #       elif if typename == 'cadence':
    #           allowed_subtypes = list(def_dict['cad_subtypes']).sort()
    #           if curr_subtypes == allowed_subtypes:
    #               valid = True
    #       elif if typename == 'homorhythm':
    #           allowed_subtypes = list(def_dict['hr_subtypes']).sort()
    #           if curr_subtypes == allowed_subtypes:
    #               valid = True
    #       #add more types later
    #       if valid:
    #           self.definition.save()
    #           super(CRIMObservation, self).save(*args, **kwargs)