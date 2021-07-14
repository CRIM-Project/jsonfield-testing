from crim.models.definition import CRIMDefinition
from crim.models.observation import CRIMObservation
from crim.serializers.definition import CRIMDefinitionSerializer
from crim.serializers.observation import CRIMObservationSerializer
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

def run():
    testobs = CRIMObservation(observer='Alice', musical_type='Fuga', 
                            details={'periodic':False,'strict':False,'flexed':False,
                            'sequential':False,'inverted':False,'retrograde':False},
                            definition=CRIMDefinition.objects.get(pk=1))
    testobs.save()