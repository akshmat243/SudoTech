from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from django.shortcuts import redirect
from .models import User

class CombinedSocialAccountAdapter(DefaultSocialAccountAdapter):
    def pre_social_login(self, request, sociallogin):
        user = sociallogin.user
        email = user.email
        provider = sociallogin.account.provider
        extra_data = sociallogin.account.extra_data

        if provider == 'google':
            full_name = extra_data.get('name') or "Google User"
            username = email.split('@')[0] if email else "user"
        elif provider == 'github':
            full_name = extra_data.get('name') or extra_data.get('login') or "GitHub User"
            username = email.split('@')[0] if email else "user"
        else:
            full_name = user.username or "User"
            username = email.split('@')[0] if email else "user"

        if email:
            try:
                existing_user = User.objects.get(email=email)

                if not existing_user.name:
                    existing_user.name = full_name
                if not existing_user.username:
                    existing_user.username = username

                existing_user.is_email_verified = True
                existing_user.save()

                sociallogin.connect(request, existing_user)
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
                return '/UserMGMT/login/'  # Inactive user fallback
            return f'/UserMGMT/dashboard/{user.username}/'
        return '/UserMGMT/login/'
