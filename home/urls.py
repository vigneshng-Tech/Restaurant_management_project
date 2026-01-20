from django.urls import path
from .views import MenuICategoryListView, MenuItemIngredientsView


urlpatterns = [
    path('menu-categories/', MenuCategoryListView.as_view(), name='menu-categories'),
    
    path(
        'api/menu-items/<int:pk>/ingredients/',
        MenuItemIngredientsView.as_view().
        name= 'menu-item-ingredients'
    ),
]