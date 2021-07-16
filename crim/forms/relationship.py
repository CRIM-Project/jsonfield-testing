from django import forms
from django.forms import ModelForm
from crim.models.relationship import CRIMRelationship

class RelationshipForm(ModelForm):
    class Meta:
        model = CRIMRelationship
        fields=['observer', 'relationship_type', 'musical_type', 'details']
        
