from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import token_obtain_pair, token_refresh

from User.views import RegisterUserViewSet, UserViewSet, my_token_obtain_pair

router = routers.SimpleRouter()
router.register('register', RegisterUserViewSet)
router.register('', UserViewSet)

urlpatterns = (
    path('token/', my_token_obtain_pair, name='token_obtain_pair'),
    path('token/refresh/', token_refresh, name='token_refresh'),

    path('', include(router.urls)),
)
