from rest_framework import serializers
from crim.models.relationship import CRIMRelationship
from crim.models.observation import CRIMObservation
from crim.serializers.observation import CRIMObservationSerializer


class CRIMRelationshipSerializer(serializers.HyperlinkedModelSerializer):
    model_observation = CRIMObservationSerializer(read_only=True)
    derivative_observation = CRIMObservationSerializer(read_only=True)

    class Meta:
        model = CRIMRelationship
        fields = ['url', 'id', 'relationship_type', 'musical_type', 'details', 'model_observation', 'derivative_observation']

    def create(self, validated_data):
        """
        Create and return a new `CRIMRelationship` instance, given the validated data.
        """
        return CRIMRelationship.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `CRIMRelationship` instance, given the validated data.
        """
        instance.relationship_type = validated_data.get('relationship_type', instance.relationship_type)
        instance.musical_type = validated_data.get('musical_type', instance.musical_type)
        instance.details = validated_data.get('details', instance.details)
        instance.model_observation = validated_data.get('model_observation', instance.model_observation)
        instance.derivative_observation = validated_data.get('derivative_observation', instance.derivative_observation)
        instance.save()
        
        return instance