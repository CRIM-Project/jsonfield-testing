from django.shortcuts import get_object_or_404, redirect
from django.http import Http404
from crim.models.relationship import CRIMRelationship
from crim.serializers.relationship import CRIMRelationshipSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer

class RelationshipList(APIView):
    """
    List all observation, or create a new observation.
    """
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'relationship_list.html'

    def get(self, request, format=None):
        relationships = CRIMRelationship.objects.all()
        return Response({'relationships': relationships}, template_name='relationship_list.html')

    def post(self, request, format=None):
        serializer = CRIMRelationshipSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, format=None):
        relationships = CRIMRelationship.objects.all()
        relationships.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class RelationshipDetail(APIView):
    """
    Retrieve, update or delete an observation.
    """
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'relationship_detail.html'

    def get(self, request, pk):
        relationship = get_object_or_404(CRIMRelationship, pk=pk)
        serializer = CRIMRelationshipSerializer(relationship, context={'request': request})
        return Response({'serializer': serializer, 'relationship': relationship}, template_name='relationship_detail.html')

    def post(self, request, pk):
        relationship = get_object_or_404(CRIMRelationship, pk=pk)
        serializer = CRIMRelationshipSerializer(relationship, data=request.data)
        if not serializer.is_valid():
            return Response({'serializer': serializer, 'relationship': relationship})
        serializer.save()
        return redirect('crimrelationship-list')
    
    def put(self, request, pk, format=None):
        relationship = self.get_object(pk)
        serializer = CRIMRelationshipSerializer(relationship, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        relationship = self.get_object(pk)
        relationship.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

class RelationshipListJSON(APIView):
    """
    List all relationships in json.
    """
    renderer_classes = [JSONRenderer]

    def get(self, request, format=None):
        relationships = CRIMRelationship.objects.all()
        serializer = CRIMRelationshipSerializer(relationships, many=True, context={'request':request})
        return Response(serializer.data)
        

class RelationshipDetailJSON(APIView):
    """
    List one relationship in json.
    """
    renderer_classes = [JSONRenderer]

    def get(self, request, pk):
        relationship = get_object_or_404(CRIMRelationship, pk=pk)
        serializer = CRIMRelationshipSerializer(relationship, context={'request': request})
        return Response(serializer.data)
