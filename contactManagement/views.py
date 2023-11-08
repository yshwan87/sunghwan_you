from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.views.generic import (
    ListView,
    CreateView,
    DetailView,
    UpdateView,
    DeleteView,
)

from django.urls import reverse_lazy
from .models import Contact

def home(request):
    contacts = [
        {
            'name': 'John Doe',
            'email': 'john.doe@example.com',
            'created_time': '2023-11-06 10:30:00',
        },
        {
            'name': 'Jane Smith',
            'email': 'jane.smith@example.com',
            'created_time': '2023-11-05 15:45:00',
        },
        {
            'name': 'Alice Johnson',
            'email': 'alice.johnson@example.com',
            'created_time': '2023-11-04 08:20:00',
        },
        # Add more contact data as needed
    ]

    context = {
        'contacts': contacts,
    }
        
    return render(request, "contactManagement/home.html", context)



class ContactListView(ListView):
    model = Contact


# class IndexView(generic.ListView):
#     template_name = "home.html"
#     context_object_name = "contact_list"

#     def get_queryset(self):
#         """Return the last five published questions."""
#         return Question.objects.order_by("-publish_date")[:5]


# # class IndexView(generic.ListView):
# #     template_name = "contactMananament/home.html"
    
# # Create your views here.
