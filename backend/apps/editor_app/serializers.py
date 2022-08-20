from abc import ABC

from django.utils.translation import gettext_lazy as _
from models import Project, Element
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
        fields = ["id", "position", "height", "width", "type", "item_list"]
