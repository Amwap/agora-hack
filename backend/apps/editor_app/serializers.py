from abc import ABC

from django.utils.translation import gettext_lazy as _
from models import Project, Element, ElementTemplate
from rest_framework import serializers


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        exclude = "main_frame"


class ElementListingField(serializers.RelatedField, ABC):
    def to_representation(self, value):
        return ElementSerializer(value)


class ElementSerializer(serializers.ModelSerializer):
    item_list = ElementListingField(many=True)

    class Meta:
        model = Element
        fields = ["id", "position", "height", "width", "type", "item_list", "styles"]

    def validate(self, data):
        parent_id = data["parent_id"]
        if parent_id is None:
            queryset = Element.objects.filter(parent_element__isnull=True)
            if queryset:
                raise serializers.ValidationError("Main frame exists already.")
        try:
            Element.objects.get(pk=data["parent_id"])
        except Element.DoesNotExist:
            raise serializers.ValidationError("Such element does not exist.")
        return data

    def create(self, validated_data):
        parent_element = None \
            if validated_data.parent_id is None \
            else Element.objects.get(pk=validated_data.parent_id)

        return Element(
            parent_element=parent_element,
            position=validated_data.position,
            type=validated_data.type,
            styles=validated_data.styles
        )


class ElementTemplateSerializer(serializers.ModelSerializer):
    element = ElementSerializer()

    class Meta:
        model = ElementTemplate
        fields = ["id", "name", "element"]
