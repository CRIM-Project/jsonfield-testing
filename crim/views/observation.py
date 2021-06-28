from django.shortcuts import get_object_or_404, redirect
from django.http import Http404
from crim.models.observation import CRIMObservation
from crim.serializers.observation import CRIMObservationSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.renderers import TemplateHTMLRenderer

class ObservationList(APIView):
    """
    List all observation, or create a new observation.
    """
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'observation_list.html'

    def get(self, request, format=None):
        observations = CRIMObservation.objects.all()
        queryset = CRIMObservation.objects.all()
        return Response({'observations': queryset}, template_name='observation_list.html')

    def post(self, request, format=None):
        serializer = CRIMObservationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, format=None):
        observations = CRIMObservation.objects.all()
        observations.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ObservationDetail(APIView):
    """
    Retrieve, update or delete an observation.
    """
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'observation_detail.html'

    def get(self, request, pk):
        observation = get_object_or_404(CRIMObservation, pk=pk)
        serializer = CRIMObservationSerializer(observation, context={'request': request})
        return Response({'serializer': serializer, 'observation': observation}, template_name='observation_detail.html')

    def post(self, request, pk):
        observation = get_object_or_404(CRIMObservation, pk=pk)
        serializer = CRIMObservationSerializer(observation, data=request.data)
        if not serializer.is_valid():
            return Response({'serializer': serializer, 'observation': observation})
        serializer.save()
        return redirect('crimobservation-list')
    
    def put(self, request, pk, format=None):
        observation = self.get_object(pk)
        serializer = CRIMObservationSerializer(observation, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        observation = self.get_object(pk)
        observation.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
#TODO: Move this to a separate home view
@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'observations': reverse('crimobservation-list', request=request, format=format),
        'relationships': reverse('crimrelationship-list',request=request, format=format)
    })