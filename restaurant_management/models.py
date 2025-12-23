from django.db import models

class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()

    has_delievery = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name

class NutritionalInformation(models.Model):

    menu_item = models.ForeignKey(
        'MenuoItem'
        on_delete=models.CASCADE
    )
    calories = models.IntegerField()
    protein_grams = models.DecimalField(max_digits=5, decimal_places=2)
    fat_grams = models.DecimalField(max_digits=5, decimal_places=2)
    carbohydrate_grams = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.menu_item} - {self.calories}kcal"