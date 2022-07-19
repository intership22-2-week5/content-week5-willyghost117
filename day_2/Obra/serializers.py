from dataclasses import field, fields
from rest_framework import serializers

"""Models"""
from .models import Author, Category, Obra

class AuthorSerializer (serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

class CategorySerializer (serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ObraSerializer (serializers.ModelSerializer):
    class Meta:
        model = Obra
        exclude = ('id',)
        
        def to_representation(self, instance):
            return {
                'id': instance.id,
                'nombre': instance.nombre,
                'authorId' : {
                'id':instance.id,
                'name': instance.name
            },
                'categoryId': instance.Category.name
        }