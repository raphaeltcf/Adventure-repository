from django.shortcuts import render
from rest_framework import viewsets
from .models import User, Address
from .serializer import UserSerializer, AddressSerializer
from .service import UserService


class UserViewSet(viewsets.ModelViewSet):
    
    serializer_class = UserSerializer

    def get_queryset(self):
        return UserService().list_users()
    
    def get_object(self):
        obj = UserService().get_user(self.kwargs['pk'])
        self.check_object_permissions(self.request, obj)
        return obj
    
    def create(self, request, *args, **kwargs):
        return UserService().create_user(request.data)
    
    def update(self, request, *args, **kwargs):
        return UserService().update_user(self.kwargs['pk'], request.data)
    
    def destroy(self, request, *args, **kwargs):
        return UserService().delete_user(self.kwargs['pk'])

class AddressViewSet(viewsets.ModelViewSet):
    serializer_class = AddressSerializer

    def get_queryset(self):
        return UserService().list_addresses()
    
    def get_object(self):
        obj = UserService().get_address(self.kwargs['pk'])
        self.check_object_permissions(self.request, obj)
        return obj
    
    def create(self, request, *args, **kwargs):
        return UserService().create_address(request.data)
    
    def update(self, request, *args, **kwargs):
        return UserService().update_address(self.kwargs['pk'], request.data)
    
    def destroy(self, request, *args, **kwargs):
        return UserService().delete_address(self.kwargs['pk'])