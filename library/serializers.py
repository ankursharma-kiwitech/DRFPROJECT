from .models import *
from rest_framework import serializers
from library.models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'description', 'price', 'stock']

    title = serializers.CharField(max_length=100)
    author = serializers.CharField(max_length=100)
    description = serializers.CharField(max_length=100)
    stock = serializers.CharField(max_length=100)
    price = serializers.CharField(max_length=100)
