from django.shortcuts import render
from rest_framework import generics
from .models import *
from .serializers import *
from django.contrib.auth.models import User
# Create your views here.




class UserCreateList(generics.ListCreateAPIView):

    queryset = User.objects.all()

    serializer_class = UserSerializer

class UserReadUpdate(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class CupboardCreateList(generics.ListCreateAPIView):
    queryset = Cupboard.objects.all()
    serializer_class = CupboardSerializer

class CupboardReadUpdate(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cupboard.objects.all()
    serializer_class = CupboardSerializer


class DressCreateList(generics.ListCreateAPIView):
    queryset = Dress.objects.all()
    serializer_class = DressSerializer

class DressReadUpdate(generics.RetrieveUpdateDestroyAPIView):
    queryset = Dress.objects.all()
    serializer_class = DressSerializer


class ListTops(generics.ListAPIView):
    # must set id 1 to tops in db
    queryset = Dress.objects.filter(prediction__id=1)
    serializer_class = DressSerializer

class ListBottoms(generics.ListAPIView):
    queryset = Dress.objects.filter(prediction__id=2)
    serializer_class = DressSerializer