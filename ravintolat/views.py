from ravintolat.models import Ravintola
from ravintolat.permissions import IsOwnerOrReadOnly
from ravintolat.serializers import RavintolaSerializer
from django.contrib.auth.models import User
from ravintolat.serializers import UserSerializer
from rest_framework import generics
from rest_framework import permissions


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class RavintolaList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Ravintola.objects.all()
    serializer_class = RavintolaSerializer
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class RavintolaDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    queryset = Ravintola.objects.all()
    serializer_class = RavintolaSerializer
