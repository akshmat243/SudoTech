from rest_framework import serializers
from .models import QuizCategory, Quiz, QuizQuestion, QuizParticipant, QuizResult


class QuizCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = QuizCategory
        fields = '__all__'


class QuizQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuizQuestion
        fields = '__all__'


class QuizSerializer(serializers.ModelSerializer):
    category = QuizCategorySerializer(read_only=True)
    questions = QuizQuestionSerializer(many=True, read_only=True)

    class Meta:
        model = Quiz
        fields = '__all__'


class QuizParticipantSerializer(serializers.ModelSerializer):
    quiz = QuizSerializer(read_only=True)

    class Meta:
        model = QuizParticipant
        fields = '__all__'


class QuizResultSerializer(serializers.ModelSerializer):
    participant = QuizParticipantSerializer(read_only=True)
    question = QuizQuestionSerializer(read_only=True)

    class Meta:
        model = QuizResult
        fields = '__all__'
