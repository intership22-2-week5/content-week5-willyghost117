from django.db import models

# Create your models here.

class Author(models.Model):
  """
  Model representing an author.
  """
  name = models.CharField(max_length=50)
  country = models.CharField(max_length=50)



class Category (models.Model):
    """Tipos de obra Model"""
    name = models.CharField(max_length=50)



class Obra(models.Model):
    """Obra model"""
    name = models.CharField(max_length=50)
    authorId = models.ForeignKey(Author,on_delete=models.CASCADE)
    categoryId = models.ForeignKey(Category,on_delete=models.CASCADE)




