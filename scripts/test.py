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
    testdef.observation_definition = {
        "cadence": {
            "tone": {
                "radio" : ["C","D","E","E-flat","F","G","A","B","B-flat"]
            },
            "type": {
                "radio" : ["Authentic", "Plagal", "Phrygian"]
            },
            "voices": "text",
            "dovetail cadence": "boolean",
            "dovetail cadence voice": "text",
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
            "regularity" : {
                "radio": ["Strict", "Flexed", "Flexed tonal"]
            },
            "invertible counterpoint": "boolean",
        },
        "non-imitative duos": {
            "voices": "text",
            "entry intervals": "text",
            "time intervals": "text",
            "regularity" : {
                "radio": ["Strict", "Flexed", "Flexed tonal"]
            },
            "invertible counterpoint": "boolean"
        },
        "periodic entries": {
            "voices": "text",
            "entry intervals": "text",
            "time intervals": "text",
            "regularity" : {
                "radio": ["Strict", "Flexed", "Flexed tonal"]
            },
            "invertible counterpoint": "boolean",
            "sequential": "boolean",
            "added entries": "boolean",
        },
        "homorhythm": {
            "voices": "text",
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
    }

    testdef.save()