from rest_framework import serializers
from.models import Ingredient

class IngredientSerializer(serializers.Modelserializer):
    class Meta:
        model = Ingredient
        fields =['id', 'name']
        