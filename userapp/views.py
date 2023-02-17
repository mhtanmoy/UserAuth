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
    #filterset_fields = ['id', 'name', 'email']
    search_fields = ['id', 'name', 'email']
    ordering_fields = ['id', 'name', 'email']
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self):
        if self.action == 'create':
            return UserAccountCreateSerializer
        return UserAccountSerializer

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
            return ResponseWrapper(
                error_code=500,
                error_message=str(e),
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    def retrieve(self, request, *args, **kwargs):
        try:
            useraccount = UserAccount.objects.filter(id=kwargs['pk']).first()
            if useraccount is None:
                return ResponseWrapper(
                    error_code=404,
                    error_message='User not found',
                    status=status.HTTP_404_NOT_FOUND
                )
            serializer = self.get_serializer(useraccount)
            return ResponseWrapper(data=serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return ResponseWrapper(
                error_code=500,
                error_message=str(e),
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    def create(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                serializer_class = UserAccountSerializer(serializer.instance).data
                return ResponseWrapper(data=serializer_class, status=status.HTTP_201_CREATED)
            print(serializer.errors)
            return ResponseWrapper(
                error_code=400,
                message=serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
        except Exception as e:
            print(e)
            return ResponseWrapper(
                error_code=500,
                error_message=str(e),
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
            

    def partial_update(self, request, *args, **kwargs):
        try:
            useraccount = UserAccount.objects.filter(id=kwargs['pk']).first()
            if useraccount is None:
                return ResponseWrapper(
                    error_code=404,
                    error_message='User not found',
                    status=status.HTTP_404_NOT_FOUND
                )
            serializer = self.get_serializer(useraccount, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                serializer_class = UserAccountSerializer(serializer.instance).data
                return ResponseWrapper(data=serializer_class, status=status.HTTP_200_OK)
            return ResponseWrapper(
                error_code=400,
                message=serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
        except Exception as e:
            return ResponseWrapper(
                error_code=500,
                error_message=str(e),
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
            
    def destroy(self, request, *args, **kwargs):
        try:
            useraccount = UserAccount.objects.filter(id=kwargs['pk']).first()
            if useraccount is None:
                return ResponseWrapper(
                    error_code=404,
                    error_message='User not found',
                    status=status.HTTP_404_NOT_FOUND
                )
            useraccount.delete()
            return ResponseWrapper(status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return ResponseWrapper(
                error_code=500,
                error_message=str(e),
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


