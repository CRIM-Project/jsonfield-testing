from django.http import HttpResponse
from django.shortcuts import render
import json

from crim.forms.relationship import RelationshipForm
from crim.models.definition import CRIMDefinition

def get_relationship(request):
    curr_def = CRIMDefinition.objects.get(pk=6)
    curr_types = list(curr_def.relationship_definition)
    first_type = curr_types[0]
    other_types = curr_types[1:]
    first_details = list(curr_def.relationship_definition[first_type].keys())
    #['test1', 'test2']
    first_details_type = list(curr_def.relationship_definition[first_type].values())
    #['boolean', 'text']
    
    
    subtype_dict = curr_def.relationship_definition

    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = RelationshipForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            form.save()
            return HttpResponse('Your relationship instance is saved')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = RelationshipForm()

    return render(request, 'relationship_form.html', 
                context={'form': form, 
                        'first_type': first_type, 
                        'other_types': other_types, 
                        'first_details': first_details,
                        'first_details_type': first_details_type,
                        'curr_types': curr_types,
                        'subtype_dict': subtype_dict, 
                        'curr_def': curr_def})
 
    