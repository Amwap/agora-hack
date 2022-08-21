from abc import ABC
from logging import root

from django.utils.translation import gettext_lazy as _
from apps.editor_app.models import Item, Project
from rest_framework import serializers



class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'

class ProjectListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('id', 'title', 'root_canvas', 'created_at', 'last_edit')


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = [
            'active',
            'deleted',
            'styles',
            'item_list',
            'element_type',
        ]

    def validate(self, attrs:dict[str, any]) -> any:
        attrs = super().validate(attrs)
        return attrs

class CreateProjectSerializer(ItemSerializer):
    class Meta:
        model = Item
        exclude = ['item_list']


    def validate(self, attrs:dict[str, any]) -> any:
        attrs = super().validate(attrs)
        return attrs

    def create(self):
        print(self.validated_data, 'HERE'*10)
        data = self.validated_data
        from pprint import pprint as pp
        pp(data)
        item = Item.objects.create(**data)
        project = Project.objects.create(
            root_canvas = item
        )
        project.title = f'Untitled project #{project.id}'
        project.save()
        return project


        



class ItemListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'

# class ItemTreeSerializer(serializers.ModelSerializer):
#     leaf_nodes = serializers.SerializerMethodField()

#     class Meta:
#         depth = 100
#         model = TreeNode
#         fields = ()

#     def get_leaf_nodes(self, obj):
#         return TreeNodeSerializer(obj.get_children(), many=True).data



# class ProjectSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Project
#         exclude = ("main_frame", )


# class ElementSerializer(serializers.ModelSerializer):
#     item_list = serializers.SerializerMethodField()

#     class Meta:
#         model = Element
#         fields = ["id", "position", "type", "styles", "item_list"]

#     def get_item_list(self):
#         return [ElementSerializer(i) for i in Element.objects.filter(parent_element=self)]

#     def validate(self, data):
#         parent_id = data["parent_id"]
#         if parent_id is None:
#             queryset = Element.objects.filter(parent_element__isnull=True)
#             if queryset:
#                 raise serializers.ValidationError("Main frame exists already.")
#         try:
#             Element.objects.get(pk=data["parent_id"])
#         except Element.DoesNotExist:
#             raise serializers.ValidationError("Such element does not exist.")
#         return data

#     def create(self, validated_data):
#         parent_element = None \
#             if validated_data.parent_id is None \
#             else Element.objects.get(pk=validated_data.parent_id)

#         return Element(
#             parent_element=parent_element,
#             position=validated_data.position,
#             type=validated_data.type,
#             styles=validated_data.styles
#         )


# class ElementTemplateSerializer(serializers.ModelSerializer):
#     element = ElementSerializer()

#     class Meta:
#         model = ElementTemplate
#         fields = ["id", "name", "element"]
