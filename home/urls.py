from .views import MenuItemIngredientsView

urlpatterns += [
    path(
        'api/menu-items/<int:pk>/ingredients/',
        MenuItemIngredientsView.as_view().
        name= 'menu-item-ingredients'
    ),
]