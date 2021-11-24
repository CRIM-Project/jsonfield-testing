from crim.models.definition import CRIMDefinition
from crim.models.observation import CJObservation
from crim.models.relationship import CJRelationship

def run():
    # testobs1 = CJObservation(observer='Evan', musical_type='Fuga',
    #                        details={'periodic':False, 'strict':False, 'flexed':False, 'sequential':False, 'inverted':False, 'retrograde':False},
    #                        definition=CRIMDefinition.objects.get(pk=5))
    # testobs1.save()
    testdef = CRIMDefinition.objects.get(id=7)
    # testdef.observation_definition['cadence']['dovetail position']['radio'] = ['Above', 'Between', 'Below']
    # testdef.save()
