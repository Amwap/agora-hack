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
        project.save()
        main_frame = Element(parent_element=None, position=None, height=None, wigth=1, type="canvas")
        main_frame.save()
        project.main_frame = main_frame
        return Response(status=200)


class ProjectsView(APIView):

    def get(self, request):
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)


class CreateElement(APIView):
    parser_classes = [JSONParser, ]

    def post(self, request, project_id):
        project = Project.objects.get(id=project_id)
        data = request.data
        parent_id = data.parent_id
        parent = Element.objects.get(id=parent_id)
        data.pop("parent_id")
        data["parent"] = parent
        serializer = ElementSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        element = serializer.create(data)
        element.project = project
        element.save()
        return Response(status=200)


class ElementsView(APIView):

    def get(self, request, project_id):
        project = Project.objects.get(id=project_id)
        main_frame = project.main_frame
        serializer = ElementSerializer(main_frame)
        return Response(serializer.data)

