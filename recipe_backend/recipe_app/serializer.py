from .models import *
from rest_framework import serializers

class FoodSerializers(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = ['name', 'type', 'datePurchased', 'daysBeforeExpire' ]

class ShoppingListItemSerializers(serializers.ModelSerializer):
    class Meta:
        model = ShoppingListItem
        fields = ['name', 'type', 'daysBeforeExpire' ]

class RecipeSerializers(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = ['id', 'name', 'imageUrl']

class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'imageUrl']