from models import Project, Element, ElementTemplate
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from serializers import ProjectSerializer, ElementSerializer, ElementTemplateSerializer
from django.forms.models import model_to_dict


class CreateProjectView(APIView):
    parser_classes = [JSONParser, ]

    def post(self, request):
        data = request.data
        serializer = ProjectSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        project = serializer.create(data)
        project.save()

        main_frame = Element(parent_element=None,
                             position=0,
                             type="canvas",
                             deleted=False,
                             styles={"value": '',
                                     "height": 0,
                                     "width": 0,
                                     "width_grid": 5,
                                     "classes": ['d-flex align-items-center justify-content-center flex-wrap']}
                             )
        main_frame.save()
        project.main_frame = main_frame
        main_frame_json = model_to_dict(main_frame)
        main_frame_json["active"] = False
        return Response(data={"id": project.id, "main_frame": main_frame_json}, status=status.HTTP_200_OK)


class ProjectsView(APIView):

    def get(self, request):
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)


class CreateElement(APIView):
    parser_classes = [JSONParser, ]

    def post(self, request, project_id):

        try:
            project = Project.objects.get(pk=project_id)
        except Project.DoesNotExist:
            return Response(data={}, status=status.HTTP_404_NOT_FOUND)

        data = request.data
        serializer = ElementSerializer(data=data)
        serializer.is_valid(raise_exception=True)

        if "id" in data:
            try:
                element = Element.objects.get(pk=data.id)
            except Element.DoesNotExist:
                return Response(data={}, status=status.HTTP_404_NOT_FOUND)
            element = serializer.update(element, data)
        else:
            element = serializer.create(data)
            element.project = project

        element.save()
        return Response(data={"id": element.id}, status=status.HTTP_200_OK)


class ElementsView:

    def get(self, request, project_id):

        try:
            project = Project.objects.get(pk=project_id)
        except Project.DoesNotExist:
            return Response(data={}, status=status.HTTP_404_NOT_FOUND)

        main_frame = project.main_frame
        serializer = ElementSerializer(main_frame)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ElementTemplatesView(APIView):
    parser_classes = [JSONParser, ]

    def get(self, request):
        element_templates = ElementTemplate.objects.all()
        serializer = ElementTemplateSerializer(element_templates, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

# class CreateElementTemplateView(APIView):
#     parser_classes = [JSONParser, ]
#
#     def post(self, request, project_id):
#
#         try:
#             project = Project.objects.get(pk=project_id)
#         except Project.DoesNotExist:
#             return Response(data={}, status=status.HTTP_404_NOT_FOUND)
#
#         data = request.data
#         parent_id = data.parent_id
#
#         try:
#             parent = Element.objects.get(pk=parent_id)
#         except Element.DoesNotExist:
#             return Response(data={}, status=status.HTTP_404_NOT_FOUND)
#
#         data.pop("parent_id")
#         data["parent"] = None
#         serializer = ElementSerializer(data=data)
#         serializer.is_valid(raise_exception=True)
#         element = serializer.create(data)
#         element.project = project
#         element.save()
#         return Response(status=status.HTTP_200_OK)
