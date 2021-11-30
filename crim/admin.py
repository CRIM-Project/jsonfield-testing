from django.contrib import admin

from crim.models.definition import CRIMDefinition
from crim.models.observation import CRIMObservation
from crim.models.relationship import CRIMRelationship

class CRIMDefinitionAdmin(admin.ModelAdmin):
    pass
class CRIMObservationAdmin(admin.ModelAdmin):
    pass
class CRIMRelationshipAdmin(admin.ModelAdmin):
    pass

admin.site.register(CRIMDefinition, CRIMDefinitionAdmin)
admin.site.register(CRIMObservation, CRIMObservationAdmin)
admin.site.register(CRIMRelationship, CRIMRelationshipAdmin)
