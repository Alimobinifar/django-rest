from django.shortcuts import render
from django.views import View
from rest_framework.response import Response
from rest_framework.decorators import APIView
from .serializer import BookSerializer

from .models import book


class book_inf(APIView):
    def get(self, request):
        qs = book.objects.values()
        ser_data = BookSerializer(qs, many=True)
        return Response(ser_data.data)
