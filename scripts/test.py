from crim.models.definition import CRIMDefinition
from crim.models.observation import CRIMObservation
from crim.models.relationship import CRIMRelationship

def run():
    testobs1 = CRIMObservation(observer='Evan', musical_type='Fuga',
                            details={'periodic':False, 'strict':False, 'flexed':False, 'sequential':False, 'inverted':False, 'retrograde':False}, 
                            definition=CRIMDefinition.objects.get(pk=5))
    testobs1.save()

    testobs2 = CRIMObservation(observer='Dean', musical_type='Fuga',
                            details={'periodic':False, 'strict':True, 'flexed':False, 'sequential':False, 'inverted':False, 'retrograde':False}, 
                            definition=CRIMDefinition.objects.get(pk=5))

    testobs2.save()