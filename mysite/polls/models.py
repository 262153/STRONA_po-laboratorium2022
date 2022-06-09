from django.db import models

#layout bazy danych z dodatkowymi danymi
#typ posilku 
class Type(models.Model):
    type_name = models.CharField(max_length=50) 
    def __str__(self):
        return self.type_name

#skladniki posilku 
class Ingredients(models.Model):
    ingredients_name = models.CharField(max_length=50)
    def __str__(self):
        return self.ingredients_name

#rodzaj posilku 
class Meals(models.Model):
    type = models.ForeignKey(Type, on_delete=models.CASCADE) #każdy meals związany z POJEDYNCZYM type
    meals_name = models.CharField(max_length=50)
    description = models.TextField(max_length=400)
    ingredients = models.ManyToManyField(Ingredients) #relacja z ingredients(opcje takie do wyboru)
    def __str__(self):
        return self.meals_name

#ocena przepisu 
class Review(models.Model):
    Meals = models.ForeignKey(Meals, on_delete=models.CASCADE)
    review = models.CharField(max_length=100)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.review

