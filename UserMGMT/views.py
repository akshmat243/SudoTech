from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from .serializers import RegisterSerializer, AssignRoleSerializer, RoleSerializer, LoginSerializer
from .models import User,Role
from django.shortcuts import render, redirect
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken
from django.views import View
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt



class RegisterView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        return render(request, 'register.html')

    def post(self, request):
        is_json = request.content_type == 'application/json'

        if is_json:
            serializer = RegisterSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"message": "User registered successfully"}, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        form_data = {
            'name': request.POST.get('name'),
            'workspace_name': request.POST.get('workspace_name'),
            'email': request.POST.get('email'),
            'password': request.POST.get('password'),
            'confirm_password': request.POST.get('confirm_password'),
        }

        serializer = RegisterSerializer(data=form_data)
        if serializer.is_valid():
            serializer.save()
            return redirect('login')
        
        return render(request, 'register.html', {
            'form_errors': serializer.errors,
            'form_data': form_data
        })




class LoginView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        return render(request, 'login.html')

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

        return render(request, 'login.html', {'errors': serializer.errors, 'email': data.get('email')})




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



    

class CanAssignRole(permissions.BasePermission):
    def has_permission(self, request, view):
        user = request.user
        return (
            user and user.is_authenticated and (
                user.is_superuser or 
                (user.role and user.role.name in ["Admin", "Manager"])
            )
        )


class AssignRoleView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = AssignRoleSerializer
    permission_classes = [CanAssignRole]

class RoleListCreateView(generics.ListCreateAPIView):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
    permission_classes = [permissions.IsAuthenticated]


