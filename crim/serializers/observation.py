from rest_framework import serializers
from crim.models.observation import CJObservation

class CJObservationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CJObservation
        fields = ['url', 'id', 'observer', 'ema', 'musical_type', 'details']

    def create(self, validated_data):
        """Create and return a new `CJObservation` instance, given
        the validated data.
        """
        return CJObservation.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """Update and return an existing `CJObservation` instance,
        given the validated data.
        """
        instance.observer = validated_data.get('observer', instance.observer)
        instance.ema = validated_data.get('ema', instance.ema)
        instance.musical_type = validated_data.get('musical_type', instance.musical_type)
        instance.details = validated_data.get('details', instance.details)
        instance.save()

        return instance
