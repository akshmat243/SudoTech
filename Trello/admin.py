from django.contrib import admin
from .models import Board, BoardMember, List, Card, Comment, Label, CardLabel

class BoardMemberInline(admin.TabularInline):
    model = BoardMember
    extra = 1

class ListInline(admin.TabularInline):
    model = List
    extra = 1

@admin.register(Board)
class BoardAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_by', 'created_on')
    search_fields = ('name', 'created_by__username')
    list_filter = ('created_on',)
    inlines = [BoardMemberInline, ListInline]

@admin.register(BoardMember)
class BoardMemberAdmin(admin.ModelAdmin):
    list_display = ('board', 'user')
    search_fields = ('board__name', 'user__username')
    list_filter = ('board',)

class CardInline(admin.TabularInline):
    model = Card
    extra = 1

@admin.register(List)
class ListAdmin(admin.ModelAdmin):
    list_display = ('title', 'board', 'order')
    search_fields = ('title', 'board__name')
    list_filter = ('board',)
    inlines = [CardInline]

@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    list_display = ('title', 'list', 'due_date', 'created_by', 'created_on')
    search_fields = ('title', 'description')
    list_filter = ('due_date', 'list__board')
    autocomplete_fields = ['list', 'created_by']
    ordering = ('order',)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('card', 'user', 'commented_on')
    search_fields = ('content', 'card__title', 'user__username')
    list_filter = ('commented_on',)

@admin.register(Label)
class LabelAdmin(admin.ModelAdmin):
    list_display = ('name', 'color')
    search_fields = ('name',)

@admin.register(CardLabel)
class CardLabelAdmin(admin.ModelAdmin):
    list_display = ('card', 'label')
    search_fields = ('card__title', 'label__name')
    list_filter = ('label',)
