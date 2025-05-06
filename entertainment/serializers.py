from rest_framework import serializers
from .models import Playlist, Content, Customer, Coupon, Orders, OrdersSummary, Blog, CustomPage, SystemSetup


class PlaylistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Playlist
        fields = '__all__'


class ContentSerializer(serializers.ModelSerializer):
    playlist = PlaylistSerializer(read_only=True)
    
    class Meta:
        model = Content
        fields = '__all__'


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'


class CouponSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coupon
        fields = '__all__'


class OrdersSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer(read_only=True)
    content = ContentSerializer(read_only=True)
    coupon = CouponSerializer(read_only=True, required=False)
    
    class Meta:
        model = Orders
        fields = '__all__'


class OrdersSummarySerializer(serializers.ModelSerializer):
    customer = CustomerSerializer(read_only=True)
    
    class Meta:
        model = OrdersSummary
        fields = '__all__'


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'


class CustomPageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomPage
        fields = '__all__'


class SystemSetupSerializer(serializers.ModelSerializer):
    class Meta:
        model = SystemSetup
        fields = '__all__'
