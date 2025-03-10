"""
database models
"""
from django.db import models # type: ignore
from django.contrib.auth.models import ( # type: ignore
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin
)
# superuser email : admin@example.com
#superuser password : Admin@123

class UserManager(BaseUserManager):
    def create_user(self,email,password=None, **extra_field):
        if not email:
            raise ValueError("User must have an email address!!!")
        user = self.model(email=self.normalize_email(email),**extra_field)
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_superuser(self,email,password):
        user = self.create_user(email,password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField( max_length=254, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'