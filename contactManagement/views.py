from django.shortcuts import render
from django.views.generic import (
    ListView,
    CreateView,
    DetailView,
    UpdateView,
    DeleteView,
)

from django.urls import reverse_lazy
from .models import Contact
from .contact_form import ContactForm

class ContactListView(ListView):
    model = Contact

class ContactCreateView(CreateView):
    model = Contact
    form_class = ContactForm
    success_url = reverse_lazy("contact_list")

class ContactDetailView(DetailView):
    model = Contact
