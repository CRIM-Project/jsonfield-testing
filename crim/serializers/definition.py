from rest_framework import serializers
from crim.models.definition import CRIMDefinition

class CRIMDefinitionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CRIMDefinition
        fields = ['observation_definition', 'relationship_definition']

    def create(self, validated_data):
        """Create and return a new `CRIMDefinition` instance, given
        the validated data.
        """
        return CRIMDefinition.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """Update and return an existing `CRIMDefinition` instance,
        given the validated data.
        """
        instance.observation_definition = validated_data.get(
            'observation_definition',
            instance.observation_definition,
        )
        instance.relationship_definition = validated_data.get(
            'relationship_definition',
            instance.relationship_definition,
        )
        instance.save()

        return instance
