from django.db.models import Q
from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from core.views import MyModelBaseViewSet

from Contact.models import Contact
from Contact.serializers import ContactSerializer


class ContactViewSet(MyModelBaseViewSet, viewsets.ModelViewSet):
    queryset = Contact.objects
    serializer_class = ContactSerializer
    permission_classes = (AllowAny, )

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.is_authenticated:
            return queryset.filter(Q(owner=self.request.user) | Q(is_public=True))
        return queryset.filter(is_public=True)
