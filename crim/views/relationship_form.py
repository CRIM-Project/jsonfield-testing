from django.http import HttpResponse
from django.shortcuts import render
import json

from crim.forms.relationship import RelationshipForm
from crim.models.definition import CRIMDefinition

def get_relationship(request):
    curr_def = CRIMDefinition.objects.get(pk=5)
    curr_types = list(curr_def.relationship_definition)
    first_type = curr_types[0]
    other_types = curr_types[1:]
    qt_details = list(curr_def.relationship_definition[first_type])

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
                        'qt_details': qt_details,
                        'curr_types': curr_types,
                        'subtype_dict': subtype_dict, 
                        'curr_def': curr_def})
 
    