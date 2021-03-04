from django.contrib.auth import get_user_model
from rest_framework import mixins, viewsets
from rest_framework.generics import RetrieveUpdateDestroyAPIView, CreateAPIView
from rest_framework.permissions import AllowAny

from User.serializers import UserSerializer


class UserViewSet(viewsets.ViewSetMixin, RetrieveUpdateDestroyAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer

    def get_queryset(self):
        return super().get_queryset().filter(pk=self.request.user.pk)


class RegisterUserViewSet(viewsets.ViewSetMixin, CreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny, ]
