from crim.models.definition import CRIMDefinition
from crim.models.observation import CRIMObservation
from crim.models.relationship import CRIMRelationship

def run():
    #testobs1 = CRIMObservation(observer='Evan', musical_type='Fuga',
    #                        details={'periodic':False, 'strict':False, 'flexed':False, 'sequential':False, 'inverted':False, 'retrograde':False}, 
    #                        definition=CRIMDefinition.objects.get(pk=5))
    #testobs1.save()


    testdef = CRIMDefinition.objects.get(id = 7)
    #testdef.observation_definition['cadence']['dovetail position']['radio'] = ['Above', 'Between', 'Below']

    #testdef.save()
    