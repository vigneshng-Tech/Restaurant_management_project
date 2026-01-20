from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import response
from .models import MenuCategory, MenuItem
from .serializers import MenuCategorySerializer, IngredientSerializer

class MenuItemIngredientsView(RetrieveAPIView):
    queryset = MenuItem.objects.all()

    def retrieve(self, request, *args, **kwargs):
        menu_item = self.get_object()
        ingredients =menu_item.ingredients.all()
        serializer = IngredientSerializer(ingredients, many=True)
        return Response(serializer.data)