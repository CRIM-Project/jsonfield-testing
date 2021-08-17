from django.http import HttpResponse
from django.shortcuts import render
import json

from crim.forms.relationship import RelationshipForm
from crim.forms.observation import ObservationForm
from crim.models.definition import CRIMDefinition

from crim.common import *

def get_relationship(request):
    # if this is a POST request we need to process the form data
    if request.is_ajax and request.method == 'POST':
        # create a form instance and manually populate it with data from the request:
        details_dict = {}
        relationship_type = ''

        #RELATIONSHIP DETAILS
        allowed_types = list(CURRENT_DEFINITION.relationship_definition.keys())
        selected_type = request.POST['selected-tab']
        strip1 = ''.join(e for e in selected_type if e.isalnum()) #get name of active type

        for rtype in allowed_types:
            strip2 = ''.join(e for e in rtype if e.isalnum()) #get name of each allowed type
            if strip1 == strip2: #if same type
                relationship_type = relationship_type + rtype #set rela type
                allowed_subtypes = list(CURRENT_DEFINITION.relationship_definition[rtype]) #allowed subtype for it
                for subtype in allowed_subtypes: #get name of each allowed subtype
                    slug = selected_type + '-' + subtype.replace(' ', '-') 
                    details_dict[subtype.capitalize()] = request.POST[slug]
                break
        json_object = json.dumps(details_dict)  

        #OBSERVATION DETAILS
        #both existing observation
        if request.POST['model_observation'] != "" and request.POST['derivative_observation'] != "":
            form_data = {"observer": request.POST['observer'],  
                        "relationship_type": relationship_type.capitalize(),
                        "details": json_object,
                        "model_observation": request.POST['model_observation'],
                        "derivative_observation": request.POST['derivative_observation'],
                        "definition": CURRENT_DEFINITION 
                        }

        #observation(s) made new
        else:
            observation_allowed_types = list(CURRENT_DEFINITION.observation_definition.keys())
            model_details_dict = {}
            model_musical_type = ''
            derivative_details_dict = {}
            derivative_musical_type = ''
            
            #model existing and derivative made new
            if request.POST['model_observation'] != "" and request.POST['derivative_observation'] == "":
                dev_selected_type = request.POST['derivative-selected-tab']
                devstrip1 = ''.join(e for e in dev_selected_type if e.isalnum()) #get name of active derivative type

                for devtype in observation_allowed_types:
                    devstrip2 = ''.join(e for e in devtype if e.isalnum()) #get name of each allowed dev type
                    if devstrip1 == devstrip2: #if same type
                        derivative_musical_type = derivative_musical_type + devtype #set musical type
                        derivative_allowed_subtypes = list(CURRENT_DEFINITION.observation_definition[devtype]) #allowed subtype for it
                        for dev_subtype in derivative_allowed_subtypes: #get name of each allowed subtype
                            devslug = "derivative-" + dev_selected_type + '-' + subtype.replace(' ', '-') 
                    
                            # check if checkboxes need to be added to array
                            if devslug in dict(request.POST):
                                if request.POST[devslug] != "":
                                    derivative_details_dict[dev_subtype.capitalize()] = request.POST[devslug].capitalize()
                                else:
                                    derivative_details_dict[dev_subtype.capitalize()] = "None"
                            # if checkboxes to be input as array
                            else:
                                dev_allowed_options = list(CURRENT_DEFINITION.observation_definition[devtype][dev_subtype]['checkbox'])
                                dev_selected_options = []
                                for dev_option in dev_allowed_options:
                                    dev_slug_array = "derivative-" + dev_selected_type + '-' + dev_option.replace(' ', '-').lower()
                                    if dev_slug_array in dict(request.POST):
                                        dev_selected_options.append(request.POST[dev_slug_array])
                                    dev_selected_options_string = ', '.join([str(elem) for elem in dev_selected_options])
                                    derivative_details_dict[dev_subtype.capitalize()] = dev_selected_options_string
                        break
                dev_json_object = json.dumps(derivative_details_dict)
                dev_form_data = {"observer": request.POST['observer'],  
                                "musical_type": derivative_musical_type.capitalize(),
                                "details": json_object,
                                "definition": CURRENT_DEFINITION 
                                }
                derivative_form = ObservationForm(dev_form_data)
                if derivative_form.is_valid():
                    derivative_form.save()

        
        #print(form_data)
        form = RelationshipForm(form_data)
        print (form.is_bound)
        print (form.is_valid())
        print (form.errors)
        print (form.non_field_errors)
        # check whether it's valid:
        if form.is_valid():
            form.save()
            return HttpResponse('Your relationship instance is saved')
        else:
            return HttpResponse('Something is wrong with your input. Try again')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = RelationshipForm(initial={"definition": CURRENT_DEFINITION})
 
    return render(request, 'relationship_form.html',
                context={'form': form,
                        'relationship_definition': CURRENT_DEFINITION.relationship_definition,
                        'observation_definition': CURRENT_DEFINITION.observation_definition
                        })