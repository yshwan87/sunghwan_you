from django.urls import path

from .views import (
    ContactListView,
    ContactCreateView,
    ContactDetailView,
    ContactUpdateView,
    ContactDeleteView,
)


urlpatterns = [
    path("", ContactListView.as_view(), name="contact_list"),
    path("create/", ContactCreateView.as_view(), name="contact_create"),
    path("contacts/<int:pk>/", ContactDetailView.as_view(), name="contact_detail"),
    path("contacts/<int:pk>/update/", ContactUpdateView.as_view(), name="contact_update"),
    path("contacts/<int:pk>/delete/", ContactDeleteView.as_view(), name="contact_delete"),
]