from models import Project, Element
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from serializers import ProjectSerializer, ElementSerializer


class CreateProjectView(APIView):
    parser_classes = [JSONParser, ]

    def post(self, request):
        data = request.data
        serializer = ProjectSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        project = serializer.create(data)
        main_frame = Element(parent_element=None, position=None, height=None, wigth=1, type="canvas")
        project.main_frame = main_frame
        project.save()
        return Response(status=200)


class ProjectsView(APIView):

    def get(self, request):
        return Project.objects.all()


class CreateElement(APIView):
    parser_classes = [JSONParser, ]

    def post(self, request):
        data = request.data
        serializer = ElementSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        element = serializer.create(data)
        element.save()
        return Response(status=200)


class ElementsView:

    def get(self, request):
        return Element.objects.all()
