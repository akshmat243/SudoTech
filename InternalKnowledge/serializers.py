from rest_framework import serializers
from .models import Book, Article, MyArticle
from UserMGMT.models import User


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'


class MyArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyArticle
        fields = '__all__'
