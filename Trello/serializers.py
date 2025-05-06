from rest_framework import serializers
from .models import Board, BoardMember, List, Card, Comment, Label, CardLabel
from UserMGMT.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']  # Customize based on the user fields you want


class BoardSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)

    class Meta:
        model = Board
        fields = ['id', 'name', 'description', 'created_by', 'created_on']


class BoardMemberSerializer(serializers.ModelSerializer):
    board = BoardSerializer(read_only=True)
    user = UserSerializer(read_only=True)

    class Meta:
        model = BoardMember
        fields = ['id', 'board', 'user']


class ListSerializer(serializers.ModelSerializer):
    board = BoardSerializer(read_only=True)

    class Meta:
        model = List
        fields = ['id', 'board', 'title', 'order']


class CardSerializer(serializers.ModelSerializer):
    list = ListSerializer(read_only=True)
    created_by = UserSerializer(read_only=True)
    comments = serializers.PrimaryKeyRelatedField(queryset=Comment.objects.all(), many=True, read_only=True)
    labels = serializers.PrimaryKeyRelatedField(queryset=Label.objects.all(), many=True, read_only=True)

    class Meta:
        model = Card
        fields = ['id', 'list', 'title', 'description', 'due_date', 'created_by', 'order', 'created_on', 'comments', 'labels']


class CommentSerializer(serializers.ModelSerializer):
    card = CardSerializer(read_only=True)
    user = UserSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = ['id', 'card', 'user', 'content', 'commented_on']


class LabelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Label
        fields = ['id', 'name', 'color']


class CardLabelSerializer(serializers.ModelSerializer):
    card = CardSerializer(read_only=True)
    label = LabelSerializer(read_only=True)

    class Meta:
        model = CardLabel
        fields = ['id', 'card', 'label']
