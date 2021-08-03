from django import forms
from crim.models.observation import CRIMObservation
from crim.models.definition import CRIMDefinition

from crim.common import *

PIECE_CHOICES = (
    ('1', 'Piece 1'),
    ('2', 'Piece 2'),
    ('3', 'Piece 3'),
    ('4', 'Piece 4'),
)

allowed_types = list(CURRENT_DEFINITION.observation_definition.keys())

MUSICAL_TYPE_CHOICES = []
i = 1
for type in allowed_types:
    MUSICAL_TYPE_CHOICES.append((i, type))
    i=i+1

class ObservationForm(forms.ModelForm):
    #piece = forms.ChoiceField(choices=PIECE_CHOICES)
    #musical_type = forms.ChoiceField(choices=MUSICAL_TYPE_CHOICES)

    class Meta:
        model = CRIMObservation
        fields=['observer', 'details', "definition"]

    def __init__(self, *args, **kwargs):
        super(ObservationForm, self).__init__(*args, **kwargs)
        self.fields['musical_type'] = forms.ChoiceField(choices=MUSICAL_TYPE_CHOICES)