from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import serializers, views, response
from .models import Slot
from .serializers import SlotSerializer, Bookserializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework import generics
from django.http import HttpResponse
from rest_framework.generics import GenericAPIView
from rest_framework.request import Request
from rest_framework.response import Response


class SlotViewSet(generics.ListCreateAPIView):
    queryset = Slot.objects.all().order_by('-date', '-time')
    serializer_class = SlotSerializer

class UnbookedSlotsView(views.APIView):
    def get(self, request, user_id):
        unbooked_slots = Slot.objects.filter(booked=False)
        serializer = SlotSerializer(unbooked_slots, many=True)
        return response.Response(serializer.data)
        

class UserSlotsView(views.APIView):
    def get(self, request, user_id):
        user_slots = Slot.objects.filter(author=user_id)
        serializer = SlotSerializer(user_slots, many=True)
        return response.Response(serializer.data)
    
class UserBookedSlotsView(views.APIView):
    def get(self, request):
        print(request)
        user_booked_slots = Slot.objects.filter(booked_by__roll=2)
        serializer = SlotSerializer(user_booked_slots, many=True)
        return response.Response(serializer.data)
    
class Bookslot(GenericAPIView):
    serializer_class = Bookserializer

    def post(self, request : Request):
        data = request.data
        serializers =Bookserializer(data = request.data)
        
        if serializers.is_valid():    
            slot = Slot.objects.all().get(id = data["slotID"])
            slot.booked = True
            slot.save()

        return Response("success")