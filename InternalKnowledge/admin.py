from django.contrib import admin
from .models import Book, Article, MyArticle

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_date')
    search_fields = ('title', 'author', 'tags')
    list_filter = ('published_date',)


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'book', 'author', 'created_on')
    search_fields = ('title', 'content', 'author')
    list_filter = ('book', 'created_on')
    date_hierarchy = 'created_on'


@admin.register(MyArticle)
class MyArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'created_on')
    search_fields = ('title', 'content', 'notes')
    list_filter = ('user',)
