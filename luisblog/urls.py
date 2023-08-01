from django.urls import path, include
from rest_framework import routers
from luisblog import views

routers=routers.DefaultRouter()
routers.register(r'blog', views.BlogViewSet)

urlpatterns = [
    path('', include(routers.urls))
]