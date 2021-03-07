import django_filters
from django.db.models import Q
from rest_framework import viewsets, filters
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from Contact.models import Contact
from Contact.serializers import ContactSerializer


class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects
    pagination_class = PageNumberPagination
    serializer_class = ContactSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend, filters.SearchFilter,)
    filterset_fields = ('is_public', )
    search_fields = ('name', 'fone', 'email')

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.is_authenticated:
            return queryset.filter(Q(owner=self.request.user) | Q(is_public=True))
        return queryset.filter(is_public=True)
