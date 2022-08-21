from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView
from apps.editor_app.models import Project, Item
from apps.editor_app.serializers import (
    CreateProjectSerializer,
    ProjectListSerializer,
    ProjectSerializer,
    ItemSerializer,
    ItemTreeSerializer
)


class ProjectView(APIView):
    parser_classes = [JSONParser, ]

    def post(self, request):
        """ Создаёт новый проект, возвращает его id """
        serializer = CreateProjectSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        instance = serializer.create()
        data = {
            "project_id": instance.id,
            "root_id": instance.root_canvas.id
        }
        return Response(status=status.HTTP_200_OK, data=data)


class ProjectListView(ListAPIView):
    """ Возвращает список объектов """
    queryset = Project.objects.all()
    serializer_class = ProjectListSerializer


class ItemView(APIView):
    def post(self, request):
        """ Создаёт новый элемент """
        serializer = ItemSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.create()
        data = {}
        return Response(status=status.HTTP_200_OK, data=data)

    def update(self, request):
        """ Обновляет элемент """
        serializer = ItemSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.update()
        data = {}
        return Response(status=status.HTTP_200_OK, data=data)

    def delete(self, request):
        """ Удаляет элемент """
        serializer = ItemSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.delete()
        data = {}
        return Response(status=status.HTTP_200_OK, data=data)


class LayoutView(APIView):
    """ Возвращает разметку проекта """
    parser_classes = [JSONParser, ]

    def get(self, request, project_id):
        ItemTreeSerializer(data=request.data)

    def get_queryset(self):
        project_id = self.request.data.get('project_id')
        project = Project.objects.get(id=project_id)
        queryset = Item.objects.filter(project=project)
        return queryset