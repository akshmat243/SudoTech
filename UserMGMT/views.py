from rest_framework import generics, permissions
from .serializers import RegisterSerializer, AssignRoleSerializer, RoleSerializer
from .models import User,Role

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]

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


