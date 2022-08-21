from django.urls import path
from apps.editor_app.views import (
    ItemView,
    LayoutView,
    ProjectListView,
    ProjectView,
)

urlpatterns = [
    path('create/project/', ProjectView.as_view(), name='create-project-view'),
    path('get/project/', ProjectView.as_view(), name='create-project-view'),
    path('get/project_list/', ProjectListView.as_view(), name='project-list-view'),
    path('item/', ItemView.as_view(), name='project-list-view'),
    path('get/layout/<slug:project_id>', LayoutView.as_view(), name='project-list-view'),
]
