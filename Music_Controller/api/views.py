from .models import Room
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from .serializers import RoomSerializer
# Create your views here.

class RoomView(generics.ListAPIView):
    queryset = Room.objects.all() # Query Set
    serializer_class = RoomSerializer