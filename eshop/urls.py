from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from core import views

router = routers.DefaultRouter()
router.register(r'good', views.GoodViewSet, basename="goods")

urlpatterns = [
    path('admin/', admin.site.urls),
    path("order/add/", views.OrderCreate.as_view()),
    path("order/all/", views.OrderList.as_view()),
    path("order/<pk>/update/", views.OrderUpdate.as_view()),
]

urlpatterns += router.urls
