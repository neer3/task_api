from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from .serializers import task2Serializer, taskSerializer
from .models import Task_List
from django.db.models import Q
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import ListAPIView
# Create your views here.


class taskListSet(viewsets.ModelViewSet):
    queryset = Task_List.objects.all()
    serializer_class = taskSerializer
    def list(self, request, *args, **kwargs):
        temp = Task_List.objects.all();
        query = request.GET.get("q")
        if query:
            temp = temp.filter(
                Q(name = query)
            )
        serial = task2Serializer(temp,many=True)
        return Response(serial.data)