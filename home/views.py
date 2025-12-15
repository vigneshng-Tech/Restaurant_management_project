from django.shortcuts import render

# Create your views here.
from rest_framework.generics import ListAPIView
from .models import MenuCategorySerializer


class MenuCategoryListView(ListAPIView):
    class Meta:
        model = MenuCategory
        fields = ['name']

from rest_framework.generics import ListAPIView
from .models import MenuCategory
from .serializers import MenuCategorySerializer

class MenuCategoryListView(ListAPIView):
    queryset = MenuCategory.objects.all()
    serilaizer_class = MenuCategorySerializer


from django.urls import path
from .views import MenuCategoryListView

urlpatterns = [
    path('menu-Catergories/', MenuCategoryListView.as_view(), name='menu-categories'),
]