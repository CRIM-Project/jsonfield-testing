from django.http import HttpResponse
from django.shortcuts import render
import json

from crim.forms.relationship import RelationshipForm
from crim.models.definition import CRIMDefinition

from crim.common import *


def get_relationship(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = RelationshipForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            form.save()
            return HttpResponse('Your relationship instance is saved')
        else:
            return HttpResponse('Something is wrong with your input. Try again')

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
 
    