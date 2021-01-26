from rest_framework import viewsets
from rest_framework.generics import CreateAPIView
from .serializers import *
from .models import Good


class GoodViewSet(viewsets.ModelViewSet):
    queryset = Good.objects.filter(qty__gt=0)
    serializer_class = GoodSerializer

    # def get_queryset(self):
    #     return Good.objects.all()


# def test(request):
#     if request.method = "GET":
#         #...
#     elif request.method == "POST":
#         # ...

class OrderCreate(CreateAPIView):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()