from django.http import HttpResponse
from django.shortcuts import render

from crim.forms.relationship import RelationshipForm
from crim.models.definition import CRIMDefinition

def get_relationship(request):
    #test json
    json = {'exact': False,
            'monnayage' : False}
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = RelationshipForm(request.POST, initial={'details': json})
        # check whether it's valid:
        if form.is_valid():
            form.save()
            return HttpResponse('Your relationship instance is saved')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = RelationshipForm()

    return render(request, 'relationship_form.html', context={'form': form})

#TODO turn details to jsonfield input 
#ajax for form after type selection
    