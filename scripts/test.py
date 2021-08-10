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

    testdef = CRIMDefinition(
        observation_definition={
        "cadence": {
            "tone": {
                "radio" : ["C","D","E","E-flat","F","G","A","B","B-flat"]
            },
            "type": {
                "radio" : ["Authentic", "Plagal", "Phrygian"]
            },
            "voices": "text",
            "overlapping": "boolean",
            "dovetail cadence": "text",
            "dovetail position": {
                "radio": ["Above", "Between", "Below", "Not applicable"]
            },
            "irregular cadence": "boolean",
            "irregular roles": {
                "checkboxes": ["Cantizans", "Altizans", "Tenorizans", "Bassizans"]
            }
        },
        "cantus firmus": {
            "voice": "text",
            "features": {
                "radio" : ["Both Pitches and Duration", "Pitches Only", "Durations Only"]
            }
        },
        "soggetto": {
            "voice": "text",
            "features": {
                "radio" : ["Both Pitches and Duration", "Pitches Only", "Durations Only"]
            },
            "ostinato" : "boolean",
            "periodic" : "boolean"
        },
        "counter soggetto": {
            "voice": "text",
            "features": {
                "radio" : ["Both Pitches and Duration", "Pitches Only", "Durations Only"]
            },
            "ostinato" : "boolean",
            "periodic" : "boolean"
        },
        "contrapuntal duo": {
            "voices": "text"
        },
        "fuga": { 
            "voices": "text",
            "entry intervals": "text",
            "time intervals": "text",
            "regularity" : {
                "radio": ["Strict", "Flexed", "Flexed tonal"]
            },
            "periodic": "boolean",
            "sequential": "boolean",
            "inverted": "boolean",
            "retrograde": "boolean"
        },
        "imitative duos": {
            "voices": "text",
            "entry intervals": "text",
            "time intervals": "text",
            "invertible counterpoint": "boolean",
            "regularity" : {
                "radio": ["Strict", "Flexed", "Flexed tonal"]
            },
        },
        "non-imitative duos": {
            "voices": "text",
            "entry intervals": "text",
            "time intervals": "text",
            "invertible counterpoint": "boolean",
            "regularity" : {
                "radio": ["Strict", "Flexed", "Flexed tonal"]
            },
        },
        "periodic entries": {
            "voices": "text",
            "entry intervals": "text",
            "time intervals": "text",
            "invertible counterpoint": "boolean",
            "regularity" : {
                "radio": ["Strict", "Flexed", "Flexed tonal"]
            },
            "sequential": "boolean",
            "added entries": "boolean",
        },
        "homorhythm": {
            "type": {
                "radio": ["Simple", "Staggered", "Sequential", "Fauxbourdon"]
            },
            "dialogue" : "boolean"
        },
        "interval patterns": {
            "alternating 3/5": "boolean",
            "alternating 6/5": "boolean",
            "alternating 8/3": "boolean",
            "parallel 10ths": "boolean",
            "parallel 3rds": "boolean",
            "parallel 6ths": "boolean",
            "preparation": {
                "radio": ["Prepared","Unprepared"]
            },
            "suspension" : "boolean"
        }
    }, 
    relationship_definition={
        "mechanical transformation": {
            "melodically inverted": "boolean",
            "metrically shifted": "boolean",
            "retrograde": "boolean",
            "sounding of different voices": "boolean",
            "systematic augmentation": "boolean",
            "systematic diminution": "boolean",
            "transposed": "boolean",
            "transposed different amounts": "boolean"
        },
        "new material": {},
        "non-mechanical transformation": {
            "amplified": "boolean",
            "double or invertible counterpoint": "boolean",
            "embellished": "boolean",
            "melodically inverted": "boolean",
            "metrically shifted": "boolean",
            "new combination": "boolean",
            "new counter subject": "boolean",
            "old counter subject shifted metrically": "boolean",
            "old counter subject transposed": "boolean",
            "reduced": "boolean",
            "retrograde": "boolean",
            "sounding of different voices": "boolean",
            "truncated": "boolean"
        },
        "omission": {},
        "quotation": {
            "exact": "boolean",
            "monnayage": "boolean"
        },
        "self": {
            "self enchainment": "boolean",
            "self repetition": "boolean",
            "self return": "boolean"
        }
    })

    testdef.save()