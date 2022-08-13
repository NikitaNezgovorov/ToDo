from django.shortcuts import render

# Create your views here.
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from .models import User
from .serializers import UserSerializer


class UserViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, GenericViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
