from django.db import models
from django.db.models import JSONField
from crim.models.definition import CRIMDefinition

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
        typename = str(self.musical_type).lower()
        def_dict = self.definition.observation_definition
        if typename in def_dict:
            valid_sub = False
            allowed_subtypes = sorted(list(def_dict[typename]))
            curr_subtypes = sorted(list(self.details.keys()))
            if allowed_subtypes == []:
                valid_sub = True
            elif curr_subtypes == allowed_subtypes:
                valid_sub = True

            if valid_sub:
                print('validated. saving observation...')
                self.definition.save()
                super(CRIMObservation, self).save(*args, **kwargs)
            else:
                print('subtypes not valid')
        else:
            print('Error saving, typename not in allowed musical types')
