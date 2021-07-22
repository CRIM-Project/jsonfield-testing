from django import forms
from crim.models.relationship import CRIMRelationship
from crim.models.definition import CRIMDefinition

PIECE_CHOICES = (
    ('1', 'Piece 1'),
    ('2', 'Piece 2'),
    ('3', 'Piece 3'),
    ('4', 'Piece 4'),
)

#Set to definition 5
set_definition = CRIMDefinition.objects.get(pk=5)
allowed_types = list(set_definition.relationship_definition.keys())

RELATIONSHIP_TYPE_CHOICES = []
i = 1
for type in allowed_types:
    RELATIONSHIP_TYPE_CHOICES.append((i, type))
    i=i+1

class RelationshipForm(forms.ModelForm):
    #piece = forms.ChoiceField(choices=PIECE_CHOICES)

    class Meta:
        model = CRIMRelationship
        fields=['observer', 'relationship_type', 'details', 'model_observation', 'derivative_observation', "definition"]

    def __init__(self, *args, **kwargs):
        super(RelationshipForm, self).__init__(*args, **kwargs)
        self.fields['relationship_type'] = forms.ChoiceField(choices=RELATIONSHIP_TYPE_CHOICES)
        
        # jsonfield widget for details 
        # OR pop up subfields true/false select

        
        
        