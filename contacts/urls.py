from django.urls import path
from .views import contacts


urlpatterns = [
    path("manage_contacts/",view=contacts,name="manage-contacts")
]
