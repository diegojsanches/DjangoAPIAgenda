from rest_framework import viewsets

from core.views import MyModelBaseViewSet

from Contact.models import Contact
from Contact.serializers import ContactSerializer


class ContactViewSet(MyModelBaseViewSet, viewsets.ModelViewSet):
    queryset = Contact.objects
    serializer_class = ContactSerializer
