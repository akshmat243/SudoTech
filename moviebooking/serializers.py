from rest_framework import serializers
from .models import (
    MovieCast,
    SeatingLayout,
    MovieShow,
    MovieOrder,
    FoodOrder,
    BookingHistory,
    SystemSetup
)


class MovieCastSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieCast
        fields = '__all__'


class SeatingLayoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = SeatingLayout
        fields = '__all__'


class MovieShowSerializer(serializers.ModelSerializer):
    theater = SeatingLayoutSerializer()

    class Meta:
        model = MovieShow
        fields = '__all__'


class MovieOrderSerializer(serializers.ModelSerializer):
    show = MovieShowSerializer()

    class Meta:
        model = MovieOrder
        fields = '__all__'


class FoodOrderSerializer(serializers.ModelSerializer):
    movie_order = MovieOrderSerializer()

    class Meta:
        model = FoodOrder
        fields = '__all__'


class BookingHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = BookingHistory
        fields = '__all__'


class SystemSetupSerializer(serializers.ModelSerializer):
    class Meta:
        model = SystemSetup
        fields = '__all__'
