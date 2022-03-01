from django.shortcuts import render
from .models import Contact
# Create your views here.

def contacts(request):
    contacts = Contact.objects.all()
    context= {
        "data": contacts
    }
    return render(request, "contacts/manage_contacts.html",context=context)

