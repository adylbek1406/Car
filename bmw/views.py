from django.shortcuts import render
from rest_framework import viewsets

from.models import *
from.serializers import *
from rest_framework import generics


class CarListCreateViewSet(generics.ListCreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer


from django.shortcuts import render


def index(request):
    return render(request, "index.html")