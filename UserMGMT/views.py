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



# class RegisterView(APIView):
#     permission_classes = [AllowAny]

#     def get(self, request):
#         return render(request, 'auth-basic-signup.html')

#     def post(self, request):
#         is_json = request.content_type == 'application/json'

#         if is_json:
#             serializer = RegisterSerializer(data=request.data, context={'request': request})
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response({"message": "User registered successfully"}, status=status.HTTP_201_CREATED)
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
#         form_data = {
#             'name': request.POST.get('name'),
#             'username': request.POST.get('username'),
#             'email': request.POST.get('email'),
#             'password': request.POST.get('password'),
#             'confirm_password': request.POST.get('confirm_password'),
#         }

#         serializer = RegisterSerializer(data=form_data, context={'request': request})
#         if serializer.is_valid():
#             serializer.save()
#             return redirect('registration_email_sent')
        
#         return render(request, 'auth-basic-signup.html', {
#             'form_errors': serializer.errors,
#             'form_data': form_data
#         })


# from django.urls import reverse

# class LoginView(APIView):
#     permission_classes = [AllowAny]

#     def get(self, request):
#         return render(request, 'auth-basic-signin.html')

#     def post(self, request):
#         data = request.data if request.content_type == 'application/json' else request.POST
#         serializer = LoginSerializer(data=data)

#         if serializer.is_valid():
#             user = serializer.validated_data['user']
#             login(request, user)

#             refresh = RefreshToken.for_user(user)
#             access_token = str(refresh.access_token)
#             refresh_token = str(refresh)

#             if request.content_type == 'application/json':
#                 return Response({
#                     'refresh': refresh_token,
#                     'access': access_token,
#                     'email': user.email,
#                     'name': user.name
#                 }, status=status.HTTP_200_OK)

#             response = reverse('dashboard', kwargs={'username': request.user.username})
#             response.set_cookie('access', access_token, httponly=True)
#             response.set_cookie('refresh', refresh_token, httponly=True)
#             return response

#         if request.content_type == 'application/json':
#             return Response(serializer.errors, status=status.HTTP_401_UNAUTHORIZED)
        
#         error_list = []
#         for field_errors in serializer.errors.values():
#             error_list.extend(field_errors)

#         return render(request, 'auth-basic-signin.html', {'form': error_list, 'email': data.get('email')})


# class DashboardView(View):
#     def get(self, request):
#         token_str = None

#         auth_header = request.headers.get('Authorization')
#         if auth_header and auth_header.startswith('Bearer '):
#             token_str = auth_header.split(' ')[1]
#         else:
#             token_str = request.COOKIES.get('access')

#         if not token_str:
#             if self._is_api_request(request):
#                 return JsonResponse({'detail': 'Authentication credentials were not provided.'}, status=401)
#             return redirect('login')

#         try:
#             access_token = AccessToken(token_str)
#             user_id = access_token['user_id']
#             user = User.objects.get(id=user_id)
#         except Exception as e:
#             if self._is_api_request(request):
#                 return JsonResponse({'detail': 'Invalid or expired token.'}, status=401)
#             return redirect('login')

#         if self._is_api_request(request):
#             return JsonResponse({
#                 'message': 'Dashboard data fetched successfully',
#                 'user': {
#                     'id': user.id,
#                     'name': user.name,
#                     'email': user.email,
#                     'username': user.username,
#                 }
#             })

#         return render(request, 'index.html', {'user': user})

#     def _is_api_request(self, request):
#         return (
#             request.headers.get('Accept') == 'application/json' or
#             request.content_type == 'application/json'
#         )

# @method_decorator(csrf_exempt, name='dispatch')
# class LogoutView(View):
#     def post(self, request):
#         is_api = self._is_api_request(request)

#         refresh_token = request.COOKIES.get('refresh')

#         if refresh_token:
#             try:
#                 token = RefreshToken(refresh_token)
#                 token.blacklist()
#             except Exception:
#                 pass 

#         response = JsonResponse({'message': 'Logout successful'}) if is_api else redirect('login')
#         response.delete_cookie('access')
#         response.delete_cookie('refresh')

#         return response

#     def get(self, request):
#         response = redirect('login')
#         response.delete_cookie('access')
#         response.delete_cookie('refresh')
#         return response

#     def _is_api_request(self, request):
#         return (
#             request.headers.get('Accept') == 'application/json' or
#             request.content_type == 'application/json'
#         )
        


from django.views import View
from django.shortcuts import render, redirect
from .serializers import RegisterSerializer
from rest_framework import status

class RegisterView(View):
    def get(self, request):
        return render(request, 'auth-basic-signup.html')

    def post(self, request):
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

from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.urls import reverse
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import LoginSerializer

class LoginView(View):
    def get(self, request):
        return render(request, 'auth-basic-signin.html')

    def post(self, request):
        data = request.POST

        serializer = LoginSerializer(data=data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            login(request, user)

            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)
            refresh_token = str(refresh)

            response = redirect('dashboard', username=user.username)
            response.set_cookie('access', access_token, httponly=True)
            response.set_cookie('refresh', refresh_token, httponly=True)

            return response

        error_list = []
        for field_errors in serializer.errors.values():
            error_list.extend(field_errors)

        return render(request, 'auth-basic-signin.html', {
            'form': error_list,
            'email': data.get('email'),
        })


from django.views import View
from django.shortcuts import redirect
from rest_framework_simplejwt.tokens import RefreshToken, TokenError
from django.http import JsonResponse

class LogoutView(View):
    def post(self, request):
        is_api = self._is_api_request(request)

        refresh_token = request.COOKIES.get('refresh')

        if refresh_token:
            try:
                token = RefreshToken(refresh_token)
                token.blacklist()  # Optional: requires blacklist app
            except TokenError:
                pass  # Token invalid or already blacklisted

        response = JsonResponse({'message': 'Logout successful'}) if is_api else redirect('login')
        response.delete_cookie('access')
        response.delete_cookie('refresh')
        return response

    def get(self, request):
        # Logout via GET (for users who click "Logout" link)
        response = redirect('login')
        response.delete_cookie('access')
        response.delete_cookie('refresh')
        return response

    def _is_api_request(self, request):
        return (
            request.headers.get('Accept') == 'application/json' or
            request.content_type == 'application/json'
        )



from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.shortcuts import redirect
from UserMGMT.models import User, UserRole

from django.http import Http404

class AdminDashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'index.html'

    def dispatch(self, request, *args, **kwargs):
        # Get username from URL
        username = kwargs.get('username')
        if username != request.user.username:
            raise Http404("You are not authorized to view this dashboard.")

        # Allow access if superuser
        if request.user.is_superuser:
            return super().dispatch(request, *args, **kwargs)

        # Check if user has approved 'admin' role
        user_roles_qs = UserRole.objects.select_related('role').filter(user=request.user, is_approved=True)
        if not user_roles_qs.exists() or not any(ur.role.name.lower() == 'admin' for ur in user_roles_qs):
            return redirect('logout')  # or a custom access denied page

        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user

        context['current_username'] = user.username
        user_roles_qs = UserRole.objects.select_related('role').filter(user=user, is_approved=True)
        context['current_user_roles'] = [ur.role.name for ur in user_roles_qs]

        # Admin metrics
        users = User.objects.filter(is_superuser=False)
        context['users'] = [{
            'user': u,
            'roles': [r.role.name for r in UserRole.objects.filter(user=u, is_approved=True).select_related('role')],
            'is_active': u.is_active,
            'is_email_verified': u.is_email_verified,
        } for u in users]
        context['user_count'] = users.count()

        new_users = User.objects.filter(is_active=False)
        context['new_users'] = new_users
        context['new_users_count'] = new_users.count()
        context['width_user_percent'] = new_users.count() * 10

        not_verified = User.objects.filter(is_email_verified=False)
        context['not_verified_users'] = not_verified
        context['not_verified_users_count'] = not_verified.count()
        context['width_email_percent'] = not_verified.count() * 10

        assigned_role_users = User.objects.filter(userrole__is_approved=True).distinct()
        context['assigned_role_users'] = assigned_role_users
        context['assigned_role_users_count'] = assigned_role_users.count()
        context['width_role_percent'] = assigned_role_users.count() * 10

        return context







from django.http import JsonResponse
from django.views import View
from .models import UserRole, Role, User, ModelAccess, Module

class ApproveRoleView(View):
    def post(self, request, user_id, role_id):
        if not request.user.is_staff:
            return JsonResponse({'error': 'Permission denied'}, status=403)

        user = User.objects.get(id=user_id)
        role = Role.objects.get(id=role_id)

        user_role, created = UserRole.objects.get_or_create(user=user, role=role)
        user_role.is_approved = True
        user_role.save()

        return JsonResponse({'message': f'Role {role.name} approved for user {user.username}'})

class ActivateUserView(View):
    def post(self, request, user_id):
        if not request.user.is_staff:
            return JsonResponse({'error': 'Permission denied'}, status=403)

        user = User.objects.get(id=user_id)
        user.is_active = True
        user.save()

        return JsonResponse({'message': f'User {user.username} has been activated.'})

class DeactivateUserView(View):
    def post(self, request, user_id):
        if not request.user.is_staff:
            return JsonResponse({'error': 'Permission denied'}, status=403)

        user = User.objects.get(id=user_id)
        user.is_active = False
        user.save()

        return JsonResponse({'message': f'User {user.username} has been deactivated.'})

class UpdateModuleAccessView(View):
    def post(self, request, role_id, action):
        if not request.user.is_staff:
            return JsonResponse({'error': 'Permission denied'}, status=403)

        role = Role.objects.get(id=role_id)
        module_id = request.POST.get('module_id')
        module = Module.objects.get(id=module_id)

        if action == 'add':
            ModelAccess.objects.create(role=role, module=module)
            return JsonResponse({'message': f'Module {module.name} added to role {role.name}'})

        elif action == 'remove':
            ModelAccess.objects.filter(role=role, module=module).delete()
            return JsonResponse({'message': f'Module {module.name} removed from role {role.name}'})

        return JsonResponse({'error': 'Invalid action'}, status=400)




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





