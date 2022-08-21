from django.urls import include, path

from apps.editor_app.views import ProjectListView, ProjectView

urlpatterns = [
    path('create/project/', ProjectView.as_view(), name='create-project-view'),
    path('get/project/', ProjectView.as_view(), name='create-project-view'),
    path('get/project_list/', ProjectListView.as_view(), name='project-list-view'),
]
