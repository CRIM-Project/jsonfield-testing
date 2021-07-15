from crim.models.definition import CRIMDefinition
from crim.models.observation import CRIMObservation

def run():
    testdef = CRIMDefinition(observation_definition = {
                                'musical_types' : ['cantus firmus', 'soggetto', 'counter-soggetto', 'contrapuntal duo', 'fuga', 'imitative duo', 'non-imitative duo', 'periodic entry', 'cadence', 'interval patterns', 'homorhythm'],
                                'cadence' : ['type', 'tone'],
                                'fuga' : ['periodic', 'strict', 'flexed', 'sequential', 'inverted', 'retrograde'],
                                'periodic entry' : ['strict', 'flexed melodic', 'flexed rhythmic', 'sequential', 'added entry', 'invertible'],
                                'imitative duo' : ['strict', 'flexed', 'flexed rhythmic', 'invertible'],
                                'non-imitative duo' : ['strict', 'flexed', 'flexed', 'flexed rhythmic', 'invertible'],
                                'homorhythm' : ['simple', 'staggered', 'sequential', 'fauxbourdon'] }, 
                            relationship_definition = {})
    testdef.save()
    
    testobs = CRIMObservation(observer='Bob', musical_type='Fuga', 
                            details={'periodic':False,'strict':False,'flexed':False,
                            'sequential':False,'inverted':False,'retrograde':False},
                            definition=CRIMDefinition.objects.get(pk=2))
    testobs.save()