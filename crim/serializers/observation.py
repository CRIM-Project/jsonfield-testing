from rest_framework import serializers
from crim.models.observation import CRIMObservation

class CRIMObservationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CRIMObservation
        fields = ['url', 'id', 'musical_type', 'details']

    def create(self, validated_data):
        """
        Create and return a new `CRIMObservation` instance, given the validated data.
        """
        return CRIMObservation.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `CRIMObservation` instance, given the validated data.
        """
        instance.musical_type = validated_data.get('musical_type', instance.musical_type)
        instance.details = validated_data.get('details', instance.details)
        instance.save()
        
        return instance