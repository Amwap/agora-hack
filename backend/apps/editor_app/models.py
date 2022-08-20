from django.db import models
from django.utils import timezone

DATETIME_FORMAT = "%d.%m.%Y %H:%M"


class Element(models.Model):
    id = models.IntegerField(primary_key=True)
    parent_element = models.ForeignKey('self', on_delete=models.CASCADE)
    position = models.IntegerField()
    height = models.IntegerField()
    width = models.IntegerField()
    type = models.CharField()
    attributes = models.JSONField()


class Project(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(null=False, unique=True)
    created_at = models.DateTimeField("Created at", auto_now_add=True, default=timezone.now())
    last_edit = models.DateTimeField("Last edit", auto_now=True, default=timezone.now())
    main_frame = models.OneToOneField(Element, on_delete=models.CASCADE)

    @property
    def creation_datetime(self):
        return self.created_at.strftime(DATETIME_FORMAT)

    @property
    def last_edit_datetime(self):
        return self.last_edit.strftime(DATETIME_FORMAT)
