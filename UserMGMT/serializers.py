from rest_framework import serializers
from .models import User
from django.contrib.auth import authenticate
from django.utils.translation import gettext_lazy as _
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
from django.contrib.auth.tokens import default_token_generator as token_generator


class RegisterSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['name', 'username', 'email', 'password', 'confirm_password']
        extra_kwargs = {'password': {'write_only': True}}

    def validate(self, data):
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError("Passwords do not match")
        return data

    def create(self, validated_data):
        validated_data.pop('confirm_password')
        user = User.objects.create_user(**validated_data, is_active=False)  # mark inactive until verified

        request = self.context.get('request')
        current_site = get_current_site(request)
        uid = urlsafe_base64_encode(force_bytes(user.pk))
        token = token_generator.make_token(user)
        verification_link = f"http://{current_site.domain}{reverse('verify-email', kwargs={'uidb64': uid, 'token': token})}"


        subject = 'Verify Your Email'
        message = render_to_string('emails/verify_email.html', {
            'user': user,
            'verification_link': verification_link,
        })
        send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [user.email])

        return user



class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(style={'input_type': 'password'})

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        user = authenticate(request=self.context.get('request'), email=email, password=password)
        if not user:
            raise serializers.ValidationError("Invalid email or password.")

        if not user.is_email_verified:
            raise serializers.ValidationError("Please verify your email before logging in.")
        
        if not user.is_active:
            raise serializers.ValidationError("Your account is inactive. Please wait until the admin approves your account.")
        
        attrs['user'] = user
        return attrs


from rest_framework import serializers
from django.contrib.auth.models import Permission
from .models import Module, ModelAccess, Role, UserRole

class ModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Module
        fields = ['id', 'name']

class ModelAccessSerializer(serializers.ModelSerializer):
    module = ModuleSerializer()

    class Meta:
        model = ModelAccess
        fields = ['id', 'module', 'model_name']

class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = ['id', 'codename', 'name', 'content_type']

class RoleSerializer(serializers.ModelSerializer):
    permission = PermissionSerializer(many=True, read_only=True)
    modules = ModuleSerializer(many=True, read_only=True)
    model_access = ModelAccessSerializer(many=True, read_only=True)

    class Meta:
        model = Role
        fields = ['id', 'name', 'permission', 'modules', 'model_access']
        
class RoleWritableSerializer(serializers.ModelSerializer):
    permission = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Permission.objects.all(), required=False
    )
    modules = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Module.objects.all(), required=False
    )
    model_access = serializers.PrimaryKeyRelatedField(
        many=True, queryset=ModelAccess.objects.all(), required=False
    )

    class Meta:
        model = Role
        fields = ['id', 'name', 'permission', 'modules', 'model_access']




class UserRoleSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    user_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), source='user', write_only=True)

    role = RoleSerializer(read_only=True)
    role_id = serializers.PrimaryKeyRelatedField(queryset=Role.objects.all(), source='role', write_only=True)

    class Meta:
        model = UserRole
        fields = ['id', 'user', 'user_id', 'role', 'role_id']
