from django.shortcuts import render
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.views import View
from rest_framework.generics import CreateAPIView, \
    ListAPIView, UpdateAPIView, DestroyAPIView, RetrieveAPIView
from .serializers import *
from .models import Good


class GoodViewSet(viewsets.ModelViewSet):
    queryset = Good.objects.filter(qty__gt=0)
    serializer_class = GoodSerializer


class OrderCreate(CreateAPIView):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()

    def post(self, request, *args, **kwargs):
        print("Job done!")
        print("Job done!")
        print("Job done!")
        return super().post(request, *args, **kwargs)



class OrderList(ListAPIView):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
    # permission_classes = [permissions.IsAuthenticated]


class OrderRetrieve(RetrieveAPIView):
    serializer_class = OrderDetailSerializer
    queryset = Order.objects.all()
    permission_classes = [permissions.IsAuthenticated]


class OrderUpdate(UpdateAPIView):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
    

class OrderDelete(DestroyAPIView):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()    


class CategoryListView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer