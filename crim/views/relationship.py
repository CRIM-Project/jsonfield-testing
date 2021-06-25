from crim.models.relationship import CRIMRelationship
from crim.serializers.relationship import CRIMRelationshipSerializer
from rest_framework import generics

class RelationshipList(generics.ListCreateAPIView):
    """
    List all relationship, or create a new relationship.
    """
    queryset = CRIMRelationship.objects.all()
    serializer_class = CRIMRelationshipSerializer

class RelationshipDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete an relationship.
    """
    queryset = CRIMRelationship.objects.all()
    serializer_class = CRIMRelationshipSerializer
   