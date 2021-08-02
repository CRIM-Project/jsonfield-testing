from django.contrib import admin

from crim.models.definition import CRIMDefinition

class CRIMDefinitionAdmin(admin.ModelAdmin):
    pass

admin.site.register(CRIMDefinition, CRIMDefinitionAdmin)
