
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers


class ModificationDisplaySerializer(serializers.ModelSerializer):
    class Meta:
        # model = Modification
        fields = '__all__'
