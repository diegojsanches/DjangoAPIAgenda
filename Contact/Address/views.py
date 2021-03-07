from rest_framework import viewsets

from Contact.Address.models import Address
from Contact.Address.serializers import AddressSerializer


class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects
    serializer_class = AddressSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.is_authenticated:
            return queryset.filter(owner=self.request.user)
        return queryset.none()
