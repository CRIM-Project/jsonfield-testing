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

    def save(self, *args, **kwargs):
        typename = str(self.musical_type).lower()
        def_dict = self.definition.observation_definition
        typelist = def_dict['musical_types']
        if typename in typelist:
            valid_sub = False
            no_validation_needed = False #for type with no required subfields for now
            allowed_subtypes = []
            curr_subtypes = sorted(list(self.details.keys()))
            
            if typename == 'fuga':
                allowed_subtypes = sorted(list(def_dict['fg_subtypes']))
            elif typename == 'cadence':
                allowed_subtypes = sorted(list(def_dict['cad_subtypes']))
            elif typename == 'homorhythm':
                allowed_subtypes = sorted(list(def_dict['hr_subtypes']))
            elif typename == 'periodic entry':
                allowed_subtypes = sorted(list(def_dict['pe_subtypes']))
            elif typename == 'imitative duo':
                allowed_subtypes = sorted(list(def_dict['id_subtypes']))
            elif typename == 'non-imitative duo':
                allowed_subtypes = sorted(list(def_dict['nid_subtypes']))
            else:
                no_validation_needed = True

            if curr_subtypes == allowed_subtypes:
                valid_sub = True
           
            if valid_sub or no_validation_needed:
                print('validated. saving...')
                self.definition.save()
                super(CRIMObservation, self).save(*args, **kwargs)
            else:
                print('subtypes not valid')
        else:
            print('Error saving, typename not in allowed musical types')
