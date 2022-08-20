from abc import ABC

from django.utils.translation import gettext_lazy as _
from models import Project, Element, ElementTemplate
from rest_framework import serializers


class ModificationDisplaySerializer(serializers.ModelSerializer):
    class Meta:
        # model = Modification
        fields = '__all__'


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


class ElementTemplateSerializer(serializers.ModelSerializer):
    element = ElementSerializer()

    class Meta:
        model = ElementTemplate
        fields = ["id", "name", "element"]
