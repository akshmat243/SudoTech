from django.contrib import admin
from .models import QuizCategory, Quiz, QuizQuestion, QuizParticipant, QuizResult

@admin.register(QuizCategory)
class QuizCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)


@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'created_at', 'updated_at')
    search_fields = ('title',)
    list_filter = ('category',)


@admin.register(QuizQuestion)
class QuizQuestionAdmin(admin.ModelAdmin):
    list_display = ('quiz', 'question_text', 'option_1', 'option_2', 'option_3', 'option_4')
    search_fields = ('question_text',)
    list_filter = ('quiz',)


@admin.register(QuizParticipant)
class QuizParticipantAdmin(admin.ModelAdmin):
    list_display = ('user', 'quiz', 'start_time', 'end_time', 'score')
    search_fields = ('user', 'quiz__title')


@admin.register(QuizResult)
class QuizResultAdmin(admin.ModelAdmin):
    list_display = ('participant', 'question', 'selected_option', 'is_correct')
    search_fields = ('participant__user', 'question__question_text')
    list_filter = ('is_correct',)
