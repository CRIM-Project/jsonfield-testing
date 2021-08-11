from crim.models.definition import CRIMDefinition
from crim.models.observation import CRIMObservation
from crim.models.relationship import CRIMRelationship

def run():
    #testobs1 = CRIMObservation(observer='Evan', musical_type='Fuga',
    #                        details={'periodic':False, 'strict':False, 'flexed':False, 'sequential':False, 'inverted':False, 'retrograde':False}, 
    #                        definition=CRIMDefinition.objects.get(pk=5))
    #testobs1.save()

    #testobs2 = CRIMObservation(observer='Dean', musical_type='Fuga',
    #                        details={'periodic':False, 'strict':True, 'flexed':False, 'sequential':False, 'inverted':False, 'retrograde':False}, 
    #                        definition=CRIMDefinition.objects.get(pk=5))
    #testobs2.save()

    testdef = CRIMDefinition.objects.get(id = 7)
    testdef.relationship_definition = {
        "mechanical transformation": {
            "melodically inverted": "boolean",
            "metrically shifted": "boolean",
            "retrograde": "boolean",
            "sounding of different voices": "boolean",
            "systematic augmentation": "boolean",
            "systematic diminution": "boolean",
            "transposition": {
                "radio": ["Transposed", "Transposed Different Amounts"]
            },
        },
        "new material": {},
        "non-mechanical transformation": {
            "activity": {
                "radio": ["Embellished", "Reduced"]
            },
            "extent": {
                "radio": ["Amplified", "Truncated"]
            },
            "double or invertible counterpoint": "boolean",
            "melodically inverted": "boolean",
            "metrically shifted": "boolean",
            "new combination": "boolean",
            "new counter subject": "boolean",
            "old counter subject shifted metrically": "boolean",
            "old counter subject transposed": "boolean",
            "retrograde": "boolean",
            "sounding of different voices": "boolean",
        },
        "omission": {},
        "quotation": {
            "type" : {
                "radio" : ["Exact", "Monnayage"]
            }
        },
        "self": {
            "self enchainment": "boolean",
            "self repetition": "boolean",
            "self return": "boolean"
        }
    }

    testdef.save()