from rest_framework import viewsets

from Contact.Address.models import Address
from Contact.Address.serializers import AddressSerializer


class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects
    serializer_class = AddressSerializer
