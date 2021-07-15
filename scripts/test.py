from crim.models.definition import CRIMDefinition
from crim.models.observation import CRIMObservation
from crim.models.relationship import CRIMRelationship

def run():
    testrel = CRIMRelationship(observer='Fred', relationship_type='Quotation',
                            details={'exact' : True, 'monnayage' : False}, model_observation = CRIMObservation.objects.get(pk=11),
                            derivative_observation = CRIMObservation.objects.get(pk=12),
                            definition=CRIMDefinition.objects.get(pk=5))
    testrel.save()