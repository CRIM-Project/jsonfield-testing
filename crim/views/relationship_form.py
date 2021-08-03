from django.http import HttpResponse
from django.shortcuts import render
import json

from crim.forms.relationship import RelationshipForm
from crim.models.definition import CRIMDefinition

from crim.common import *

def get_relationship(request):
    curr_def = CRIMDefinition.objects.get(pk=6)
    #curr_types = list(curr_def.relationship_definition)
    
    mt_details = list(curr_def.relationship_definition['mechanical transformation'].keys())
    mt_details_type = list(curr_def.relationship_definition['mechanical transformation'].values())
    nm_details = list(curr_def.relationship_definition['new material'].keys())
    nm_details_type = list(curr_def.relationship_definition['new material'].values())
    nmt_details = list(curr_def.relationship_definition['non-mechanical transformation'].keys())
    nmt_details_type = list(curr_def.relationship_definition['non-mechanical transformation'].values())
    om_details = list(curr_def.relationship_definition['omission'].keys())
    om_details_type = list(curr_def.relationship_definition['omission'].values())
    qt_details = list(curr_def.relationship_definition['quotation'].keys())
    qt_details_type = list(curr_def.relationship_definition['quotation'].values())

    details_dict = {}

    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        details_dict = {}
        #form = RelationshipForm(initial={"definition":"6"})
        #form = RelationshipForm(request.POST, initial={"definition":"6"})
        observer = request.POST['observer']
        relationship_type = request.POST['relationship_type']
        model_observation = request.POST['model_observation']
        derivative_observation = request.POST['derivative_observation']
        type_dict = {'quotation' : 'qt', 
                    'omission' : 'om', 
                    'new material' : 'nm', 
                    'non-mechanical transformation' : 'nmt',
                    'mechanical transformation' : 'mt' }
        rela = type_dict.get(relationship_type.lower())
        print(rela)
        details_dict = {  }
        qt_quickres = request.POST['qtexact']
        form = RelationshipForm(initial={"observer": observer, 
                                        "relationship_type": relationship_type, 
                                        "model_observation": model_observation,
                                        "derivative_observation": derivative_observation,
                                        
                                        })

        

        
        # check whether it's valid:
        #if form.is_valid():
        #    form.save()
        #    return HttpResponse('Your relationship instance is saved')
        #else:
        #    return HttpResponse('Something is wrong with your input. Try again')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = RelationshipForm()

    return render(request, 'relationship_form.html', 
                context={'form': form, 
                        'mt_details': mt_details,
                        'mt_details_type': mt_details_type,
                        'nm_details': nm_details,
                        'nm_details_type': nm_details_type,
                        'nmt_details': nmt_details,
                        'nmt_details_type': nmt_details_type,
                        'om_details': om_details,
                        'om_details_type': om_details_type,
                        'qt_details': qt_details,
                        'qt_details_type': qt_details_type,
                        })
 
    return render(request, 'relationship_form.html',
                context={'form': form,
                        'relationship_definition': CURRENT_DEFINITION.relationship_definition,
                        })