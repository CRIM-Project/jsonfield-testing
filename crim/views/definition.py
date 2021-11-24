from django.shortcuts import get_object_or_404, redirect
from django.http import Http404
from crim.models.definition import CRIMDefinition
from crim.serializers.definition import CRIMDefinitionSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.reverse import reverse
#from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer

class DefinitionList(APIView):
    """List all definitions, or create a new definition."""
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'definition_list.html'

    def get(self, request, format=None):
        definitions = CRIMDefinition.objects.all()
        return Response({'definitions': definitions}, template_name='definition_list.html')

    def post(self, request, format=None):
        serializer = CRIMDefinitionSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, format=None):
        definitions = CRIMDefinition.objects.all()
        definitions.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class DefinitionDetail(APIView):
    """Retrieve, update or delete an definition."""
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'definition_detail.html'

    def get(self, request, pk):
        definition = get_object_or_404(CRIMDefinition, pk=pk)
        serializer = CRIMDefinitionSerializer(definition, context={'request': request})
        return Response({'serializer': serializer, 'definition': definition}, template_name='definition_detail.html')

    def post(self, request, pk):
        definition = get_object_or_404(CRIMDefinition, pk=pk)
        serializer = CRIMDefinitionSerializer(definition, data=request.data, context={'request': request})
        if not serializer.is_valid():
            return Response({'serializer': serializer, 'definition': definition})
        serializer.save()
        return redirect('crimdefinition-list')

    def put(self, request, pk, format=None):
        definition = self.get_object(pk)
        serializer = CRIMDefinitionSerializer(definition, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        definition = self.get_object(pk)
        definition.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class DefinitionListJSON(APIView):
    """List all definitions in json."""
    renderer_classes = [JSONRenderer]

    def get(self, request, format=None):
        definitions = CRIMDefinition.objects.all()
        serializer = CRIMDefinitionSerializer(definitions, many=True, context={'request':request})
        return Response(serializer.data)


class DefinitionDetailJSON(APIView):
    """
    List one definition in json.
    """
    renderer_classes = [JSONRenderer]

    def get(self, request, pk):
        definition = get_object_or_404(CRIMDefinition, pk=pk)
        serializer = CRIMDefinitionSerializer(definition, context={'request': request})
        return Response(serializer.data)
