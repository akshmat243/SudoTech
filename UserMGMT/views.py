from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .serializers import RegisterSerializer, LoginSerializer
from .models import User
from django.shortcuts import render, redirect
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken
from django.views import View
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth.tokens import default_token_generator as token_generator
from django.contrib import messages



class RegisterView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        return render(request, 'auth-basic-signup.html')

    def post(self, request):
        is_json = request.content_type == 'application/json'

        if is_json:
            serializer = RegisterSerializer(data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response({"message": "User registered successfully"}, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        form_data = {
            'name': request.POST.get('name'),
            'username': request.POST.get('username'),
            'email': request.POST.get('email'),
            'password': request.POST.get('password'),
            'confirm_password': request.POST.get('confirm_password'),
        }

        serializer = RegisterSerializer(data=form_data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return redirect('registration_email_sent')
        
        return render(request, 'auth-basic-signup.html', {
            'form_errors': serializer.errors,
            'form_data': form_data
        })




class LoginView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        return render(request, 'auth-basic-signin.html')

    def post(self, request):
        data = request.data if request.content_type == 'application/json' else request.POST
        serializer = LoginSerializer(data=data)

        if serializer.is_valid():
            user = serializer.validated_data['user']
            login(request, user)

            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)
            refresh_token = str(refresh)

            if request.content_type == 'application/json':
                return Response({
                    'refresh': refresh_token,
                    'access': access_token,
                    'email': user.email,
                    'name': user.name
                }, status=status.HTTP_200_OK)

            response = redirect('dashboard')
            response.set_cookie('access', access_token, httponly=True)
            response.set_cookie('refresh', refresh_token, httponly=True)
            return response

        if request.content_type == 'application/json':
            return Response(serializer.errors, status=status.HTTP_401_UNAUTHORIZED)
        
        error_list = []
        for field_errors in serializer.errors.values():
            error_list.extend(field_errors)

        return render(request, 'auth-basic-signin.html', {'form': error_list, 'email': data.get('email')})


class DashboardView(View):
    def get(self, request):
        token_str = None

        auth_header = request.headers.get('Authorization')
        if auth_header and auth_header.startswith('Bearer '):
            token_str = auth_header.split(' ')[1]
        else:
            token_str = request.COOKIES.get('access')

        if not token_str:
            if self._is_api_request(request):
                return JsonResponse({'detail': 'Authentication credentials were not provided.'}, status=401)
            return redirect('login')

        try:
            access_token = AccessToken(token_str)
            user_id = access_token['user_id']
            user = User.objects.get(id=user_id)
        except Exception as e:
            if self._is_api_request(request):
                return JsonResponse({'detail': 'Invalid or expired token.'}, status=401)
            return redirect('login')

        if self._is_api_request(request):
            return JsonResponse({
                'message': 'Dashboard data fetched successfully',
                'user': {
                    'id': user.id,
                    'name': user.name,
                    'email': user.email,
                    'workspace_name': user.workspace_name,
                }
            })

        return render(request, 'dashboard.html', {'user': user})

    def _is_api_request(self, request):
        return (
            request.headers.get('Accept') == 'application/json' or
            request.content_type == 'application/json'
        )


@method_decorator(csrf_exempt, name='dispatch')
class LogoutView(View):
    def post(self, request):
        is_api = self._is_api_request(request)

        refresh_token = request.COOKIES.get('refresh')

        if refresh_token:
            try:
                token = RefreshToken(refresh_token)
                token.blacklist()
            except Exception:
                pass 

        response = JsonResponse({'message': 'Logout successful'}) if is_api else redirect('login')
        response.delete_cookie('access')
        response.delete_cookie('refresh')

        return response

    def get(self, request):
        response = redirect('login')
        response.delete_cookie('access')
        response.delete_cookie('refresh')
        return response

    def _is_api_request(self, request):
        return (
            request.headers.get('Accept') == 'application/json' or
            request.content_type == 'application/json'
        )


def verify_email(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = User.objects.get(pk=uid)

        if token_generator.check_token(user, token):
            user.is_email_verified = True
            user.save()
            messages.success(request, 'Email verified successfully. You can now wait until the admin verifies your account.')
            return redirect('login')
        else:
            messages.error(request, 'Invalid verification link.')
    except Exception:
        messages.error(request, 'Verification failed.')

    return redirect('register')





