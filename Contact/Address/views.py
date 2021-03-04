from rest_framework import viewsets

from core.views import MyModelBaseViewSet

from Contact.Address.models import Address
from Contact.Address.serializers import AddressSerializer


class AddressViewSet(MyModelBaseViewSet, viewsets.ModelViewSet):
    queryset = Address.objects
    serializer_class = AddressSerializer
