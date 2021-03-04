from rest_framework import viewsets

from Contact.models import Contact
from Contact.serializers import ContactSerializer


class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects
    serializer_class = ContactSerializer
