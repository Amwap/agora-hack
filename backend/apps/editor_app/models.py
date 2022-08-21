from django.db import models
from enum import Enum
from mptt.models import MPTTModel, TreeForeignKey


class PositionTypes(Enum):
    CANVAS = 'canvas'
    TEXT = 'text'
    IMAGE = 'image'

    @classmethod
    def choices(cls):
        return [(i.value, i.value) for i in cls]


class Item(MPTTModel):
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    position = models.PositiveIntegerField("Position", default=0)
    active = models.BooleanField(verbose_name="Active editing", default=False)
    deleted = models.BooleanField(verbose_name="Deleted", default=False)
    styles = models.JSONField("Styles")
    item_list = models.ManyToManyField('editor_app.Project', verbose_name="Item list", null=True)
    element_type = models.CharField(verbose_name="Element type", choices=PositionTypes.choices(),
                                    default=PositionTypes.CANVAS, max_length=250)

    class Meta:
        verbose_name = 'Item'
        verbose_name_plural = 'Item list'

    class MPTTMeta:
        order_insertion_by = ['position', ]

    def __str__(self) -> str:
        return str(self.id)


class Project(models.Model):
    title = models.CharField(verbose_name="Title", max_length=250, null=True, )
    root_canvas = models.OneToOneField(Item, verbose_name="Root canvas", on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField("Created at", auto_now_add=True)
    last_edit = models.DateTimeField("Last edit", auto_now=True)

    class Meta:
        verbose_name = 'Project'
        verbose_name_plural = 'List of projects'

    def __str__(self) -> str:
        return str(self.title)
