from rest_framework import  viewsets
from .models import book
from .serializer import BookSerializer
from django.shortcuts import get_object_or_404
from rest_framework.response import Response


class BookViewset(viewsets.ModelViewSet):
    queryset = book.objects.all()
    serializer_class = BookSerializer


    # def list(self,request):
    #     qs = book.objects.all()
    #     ser_data=BookSerializer(qs, many=True)
    #     return Response(ser_data.data)
    #
    # def retrieve(self, request, pk=None):
    #     qs = book.objects.all()
    #     bk = get_object_or_404(qs, id=pk)
    #     ser_data = BookSerializer(bk)
    #     return Response(ser_data.data)
    #
    # def create(self, request):
    #     ser_data=BookSerializer(data=request.data)
    #     if ser_data.is_valid():
    #         ser_data.save()
    #         return Response({"message": "ok"})
    #     else:
    #         return Response(ser_data.errors)
    #
    # def destroy(self, request, pk=None):
    #     ser_data = BookSerializer(data=request.data)
    #     book.objects.filter(id=pk).delete()
    #     return Response({"result", "deleted success"})
    #
    # def update(self, request, pk=None):
    #     ser_data = BookSerializer(data=request.data)
    #     if ser_data.is_valid():
    #         ser_data.save()
    #         return Response({"result", "updated success"})
    #     else:
    #         return Response({"Error":"data is not in validate form"})
