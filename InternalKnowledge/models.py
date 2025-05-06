from django.db import models
from UserMGMT.models import User

class Book(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    author = models.CharField(max_length=255)
    published_date = models.DateField(null=True, blank=True)
    tags = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Article(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='articles')
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    author = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class MyArticle(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='my_articles')
    title = models.CharField(max_length=255)
    content = models.TextField()
    notes = models.TextField(blank=True)
    reference_article = models.ForeignKey(Article, null=True, blank=True, on_delete=models.SET_NULL)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
