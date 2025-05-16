from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from django.shortcuts import redirect
from .models import User

class MySocialAccountAdapter(DefaultSocialAccountAdapter):
    def pre_social_login(self, request, sociallogin):
        user = sociallogin.user
        email = user.email

        # Get data from Google
        extra_data = sociallogin.account.extra_data
        full_name = extra_data.get('name') or user.username or "User"
        username = (
            email.split('@')[0] if email else "user"
        )

        if email:
            try:
                existing_user = User.objects.get(email=email)

                # Update name and username if missing
                if not existing_user.name:
                    existing_user.name = full_name
                if not existing_user.username:
                    existing_user.username = username

                # Auto verify email
                existing_user.is_email_verified = True
                existing_user.save()

                # Connect the social account to the existing user
                sociallogin.connect(request, existing_user)

                # Set the user object for the session
                sociallogin.state['process'] = 'connect'

            except User.DoesNotExist:
                user.name = full_name
                user.username = username
                user.is_email_verified = True
                user.save()

    def get_login_redirect_url(self, request):
        user = request.user

        if user.is_authenticated:
            if not user.is_active:
                return '/UserMGMT/login/'  # Redirect if inactive
            return f'/UserMGMT/dashboard/{user.username}/'

        return '/UserMGMT/login/'  # Default fallback

