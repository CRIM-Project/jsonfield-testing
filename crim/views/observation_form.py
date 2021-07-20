from django.http import HttpResponse
from django.shortcuts import render

from crim.forms.observation import ObservationForm
#from crim.models.definition import CRIMDefinition

def get_observation(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ObservationForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            form.save()
            return HttpResponse('Your observation instance is saved')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ObservationForm()

    return render(request, 'observation_form.html', context={'form': form})