from django import forms
from splitjson.widgets import SplitJSONWidget
from crim.models.relationship import CRIMRelationship
from crim.models.definition import CRIMDefinition
from crim.models.observation import CRIMObservation

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
strkey = ''
for type in allowed_types:
    strkey = str(type)
    RELATIONSHIP_TYPE_CHOICES.append((strkey, type))

class RelationshipForm(forms.ModelForm):
    #piece = forms.ChoiceField(choices=PIECE_CHOICES)

    class Meta:
        model = CRIMRelationship
        fields=['observer', 'relationship_type', 'details', 'model_observation', 'derivative_observation', "definition"]

    def __init__(self, *args, **kwargs):
        super(RelationshipForm, self).__init__(*args, **kwargs)
        self.fields['relationship_type'] = forms.ChoiceField(choices=RELATIONSHIP_TYPE_CHOICES)
        self.fields['model_observation'] = forms.ModelChoiceField(queryset=CRIMObservation.objects.all(), widget=forms.NumberInput, required=True)
        self.fields['derivative_observation'] = forms.ModelChoiceField(queryset=CRIMObservation.objects.all(), widget=forms.NumberInput, required=True)
        
        #attrs = {'class':'special', 'size':'40'}
        #self.fields['details'] = forms.CharField(widget=SplitJSONWidget())

        # default def = 5, hide in template
        # jsonfield widget for details 
        # OR pop up subfields true/false select

        
        
        