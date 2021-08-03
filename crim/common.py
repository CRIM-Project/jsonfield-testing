from crim.models.definition import CRIMDefinition

CURRENT_DEFINITION = CRIMDefinition.objects.latest('id')