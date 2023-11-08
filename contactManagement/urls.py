from django.urls import path

from .views import (
    ContactListView,
    #ContactCreateView,
    # TaskDetailView,
    # TaskUpdateView,
    # TaskDeleteView,
)


urlpatterns = [
    path("", ContactListView.as_view(), name="contact_list"),
    path("create/", ContactListView.as_view(), name="contact_create"),
    # path("tasks/<int:pk>/", TaskDetailView.as_view(), name="task_detail"),
    # path("tasks/<int:pk>/update/", TaskUpdateView.as_view(), name="task_update"),
    # path("tasks/<int:pk>/delete/", TaskDeleteView.as_view(), name="task_delete"),
]