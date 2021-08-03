from django.contrib import admin

# Register your models here.
from crim.models.definition import CRIMDefinition

class CRIMDefinitionAdmin(admin.ModelAdmin):
    pass

admin.site.register(CRIMDefinition, CRIMDefinitionAdmin)