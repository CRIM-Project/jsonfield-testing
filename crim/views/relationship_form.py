from django.http import HttpResponse
from django.shortcuts import render
import json

from crim.forms.relationship import RelationshipForm
from crim.models.definition import CRIMDefinition

from crim.common import *

def get_relationship(request):
    # if this is a POST request we need to process the form data
    if request.is_ajax and request.method == 'POST':
        # create a form instance and manually populate it with data from the request:
        details_dict = {}
        relationship_type = ''

        allowed_types = list(CURRENT_DEFINITION.relationship_definition.keys())
        selected_type = request.POST['selected-tab']
        strip1 = ''.join(e for e in selected_type if e.isalnum())

        for rtype in allowed_types:
            strip2 = ''.join(e for e in rtype if e.isalnum())
            if strip1 == strip2:
                relationship_type = relationship_type + rtype
                allowed_subtypes = list(CURRENT_DEFINITION.relationship_definition[rtype])
                for subtype in allowed_subtypes:
                    slug = subtype.replace(' ', '-')
                    details_dict[subtype.capitalize()] = request.POST[slug]
                break
        json_object = json.dumps(details_dict)  

        form_data = {"observer": request.POST['observer'],  
                    "relationship_type": relationship_type.capitalize(),
                    "details": json_object,
                    "model_observation": request.POST['model_observation'],
                    "derivative_observation": request.POST['derivative_observation'],
                    "definition": CURRENT_DEFINITION 
                    }
        #print(form_data)
        form = RelationshipForm(form_data)
        print (form.is_bound)
        print (form.is_valid())
        print (form.errors)
        print (form.non_field_errors)
        # check whether it's valid:
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            return HttpResponse('Your relationship instance is saved')
        else:
            return HttpResponse('Something is wrong with your input. Try again')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = RelationshipForm()
 
    return render(request, 'relationship_form.html',
                context={'form': form,
                        'relationship_definition': CURRENT_DEFINITION.relationship_definition,
                        })