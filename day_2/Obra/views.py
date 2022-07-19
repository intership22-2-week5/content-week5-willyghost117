"""Djago rest"""
from rest_framework.views import Response
from rest_framework import viewsets

"""Models"""
from .models import Author, Category, Obra


"""Serializer"""
from .serializers import AuthorSerializer, CategorySerializer, ObraSerializer


# Create your views here.

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ObraViewSet (viewsets.ModelViewSet):
    queryset = Obra.objects.all()
    serializer_class = ObraSerializer

    