from django.utils.translation import gettext_lazy as _
from models import Project, Element
from rest_framework import serializers


class ModificationDisplaySerializer(serializers.ModelSerializer):
    class Meta:
        # model = Modification
        fields = '__all__'


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project


class ElementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Element