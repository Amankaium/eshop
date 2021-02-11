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
    path("order/<pk>/", views.OrderRetrieve.as_view(), name="order"),
    path("order/<pk>/update/", views.OrderUpdate.as_view()),
    path("order/<pk>/delete/", views.OrderDelete.as_view()),
    path("auth/", include('djoser.urls')),
    path("auth/", include('djoser.urls.authtoken')),
    path("auth/", include('djoser.urls.jwt')),

]

urlpatterns += router.urls
