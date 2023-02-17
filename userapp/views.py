from django.shortcuts import render
from rest_framework import permissions, status, viewsets, filters
from rest_framework.response import Response
from .models import *
from .serializers import *
from utils.response_wrapper import ResponseWrapper
from django_filters.rest_framework import DjangoFilterBackend

class UserViewSet(viewsets.ModelViewSet):
    queryset = UserAccount.objects.all()
    serializer_class = UserAccountSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['id', 'name', 'email']
    search_fields = ['id', 'name', 'email']
    ordering_fields = ['id', 'name', 'email']

    def list(self, request, *args, **kwargs):
        try:
            queryset = self.filter_queryset(self.get_queryset())
            page = self.paginate_queryset(queryset)
            if page is not None:
                serializer = self.get_serializer(page, many=True)
                return self.get_paginated_response(serializer.data)
            serializer = self.get_serializer(queryset, many=True)
            return ResponseWrapper(data=serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return ResponseWrapper(data=str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def retrieve(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            serializer = self.get_serializer(instance)
            return ResponseWrapper(data=serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return ResponseWrapper(data=str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def create(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return ResponseWrapper(data=serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        except Exception as e:
            return ResponseWrapper(data=str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def update(self, request, *args, **kwargs):
        try:
            partial = kwargs.pop('partial', False)
            instance = self.get_object()
            serializer = self.get_serializer(instance, data=request.data, partial=partial)
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)
            if getattr(instance, '_prefetched_objects_cache', None):
                instance._prefetched_objects_cache = {}
            return ResponseWrapper(data=serializer.data, status=status.HTTP_200_OK)

        except Exception as e:
            return ResponseWrapper(data=str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)


