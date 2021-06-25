from crim.models.observation import CRIMObservation
from crim.serializers.observation import CRIMObservationSerializer
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.decorators import api_view

class ObservationList(generics.ListCreateAPIView):
    """
    List all observation, or create a new observation.
    """
    queryset = CRIMObservation.objects.all()
    serializer_class = CRIMObservationSerializer

class ObservationDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete an observation.
    """
    queryset = CRIMObservation.objects.all()
    serializer_class = CRIMObservationSerializer

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'observations': reverse('crimobservation-list', request=request, format=format),
        'relationships': reverse('crimrelationship-list',request=request, format=format)
    })