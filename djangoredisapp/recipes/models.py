from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name 

class Recipe(models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE) 
    image_url = models.CharField(max_length=500)
    description = models.CharField(max_length=2000)

    def __str__(self) -> str:
        return self.name 