from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)


class ApiUserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None):
        user = self.create_user(
            email,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class ApiUser(AbstractBaseUser):
    username_validator = UnicodeUsernameValidator()

    id = models.CharField(
        verbose_name='ID',
        max_length=255,
        unique=True,
    )
    email = models.EmailField(
        'email address',
        max_length=255,
        unique=True,
        error_messages={
            'unique': "A user with that email already exists."
        }
    )
    username = models.CharField(
        'username', primary_key=True, max_length=150, blank=False, null=False, unique=True,
        help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.',
        validators=[username_validator],
        error_messages={
            'unique': "A user with that username already exists."
        },
    )
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = ApiUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['password', 'is-admin']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin
