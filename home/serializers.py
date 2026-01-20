from rest_framework import serializers
from.models import MenuCategory, Ingredient

class IngredientSerializer(serializers.Modelserializer):
    class Meta:
        model = Ingredient
        fields =['id', 'name']


class IngredientSerializer(serializers.Modelserializer):
    class MetaL:
        model = Ingredient
        fields =['id', 'name']
        