from django.urls import path
from .views import *

urlpatterns = [
    path('users/', UserViewSet.as_view({'get': 'list'})),
]
