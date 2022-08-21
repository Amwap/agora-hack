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
            'element_type',
        ]

    def validate(self, attrs: dict[str, any]) -> any:
        attrs = super().validate(attrs)
        return attrs

    def _get_item(self):
        item_id = self.validated_data.get('item_id')
        return Item.objects.get(id=item_id)

    def create(self):
        """ Создаёт новый элемент """
        parent_id = self.validated_data.get('parent_id')
        parent = Item.objects.get(id=parent_id)
        new_item = Item.objects.create(
            id=self.validated_data.get('id'),
            parent=parent,
            position=self.validated_data.get('position'),
            active=self.validated_data.get('active'),
            deleted=self.validated_data.get('deleted'),
            styles=self.validated_data.get('styles'),
            element_type=self.validated_data.get('element_type')
        )
        new_item.save()
        parent.item_list.add(new_item)
        return new_item

    def update(self):
        """ Обновляет элемент """
        item_obj = self._get_item()
        item_obj.position = self.validated_data.get('position', item_obj.position),
        item_obj.active = self.validated_data.get('active', item_obj.active),
        item_obj.deleted = self.validated_data.get('deleted', item_obj.deleted),
        item_obj.styles = self.validated_data.get('styles', item_obj.styles),
        item_obj.element_type = self.validated_data.get('element_type', item_obj.element_type)
        item_obj.save()
        return item_obj

    def delete(self):
        """ Удаляет элемент """
        item_obj = self._get_item()
        item_obj.delete()


class ItemTreeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = (
            'active',
            'deleted',
            'styles',
            'element_type',
            'item_list',
        )

    def get_fields(self):
        fields = super(ItemTreeSerializer, self).get_fields()
        fields['item_list'] = ItemTreeSerializer(many=True)
        return fields


class CreateProjectSerializer(ItemSerializer):
    class Meta:
        model = Item
        exclude = ['item_list']

    def validate(self, attrs: dict[str, any]) -> any:
        attrs = super().validate(attrs)
        return attrs

    def create(self):
        print(self.validated_data, 'HERE' * 10)
        data = self.validated_data
        item = Item.objects.create(**data)
        project = Project.objects.create(
            root_canvas=item
        )
        project.title = f'Untitled project #{project.id}'
        project.save()
        return project
