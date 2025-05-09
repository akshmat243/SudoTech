from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.conf import settings

class CustomUserManager(BaseUserManager):
    def create_user(self, email, name, workspace_name, password=None, is_active=False):
        if not email:
            raise ValueError('Users must have an email address')
        email = self.normalize_email(email)
        user = self.model(email=email, name=name, workspace_name=workspace_name, is_active=is_active)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, workspace_name, password):
        user = self.create_user(email, name, workspace_name, password)
        user.is_superuser = True
        user.is_staff = True
        user.is_active = True
        user.save(using=self._db)
        return user

    
    
class User(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=255)
    workspace_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_email_verified = models.BooleanField(default=False)


    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'workspace_name']

    def __str__(self):
        return self.email
    
class Module(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class ModelAccess(models.Model):
    module = models.ForeignKey(Module, on_delete=models.CASCADE)
    model_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.module.name} - {self.model_name}"


class Role(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class RoleModelPermission(models.Model):
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    model_access = models.ForeignKey(ModelAccess, on_delete=models.CASCADE)
    can_manage = models.BooleanField(default=False)
    can_create = models.BooleanField(default=False)
    can_edit = models.BooleanField(default=False)
    can_delete = models.BooleanField(default=False)


class UserRole(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    is_approved = models.BooleanField(default=False)
    
    def save(self, *args, **kwargs):
        if self.is_approved and not self.user.is_active:
            self.user.is_active = True
            self.user.save()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.user.email} - {self.role.name}"