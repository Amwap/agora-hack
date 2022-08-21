import os
from email.policy import default
from importlib.resources import path

from django.conf import settings
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.core.validators import RegexValidator
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, username=None, email=None, phone=None, password=None, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        if not username:
            if not email and not phone:
                raise ValueError('The given email/phone must be set')

        if email:
            email = self.normalize_email(email)

            if not username:
                username = email

            user = self.model(
                email=email,
                username=username,
                **extra_fields
            )

        if phone:
            if not username:
                username = phone

            user = self.model(
                username=username,
                phone=phone,
                **extra_fields
            )

        # проверяем является ли пользователь
        # суперпользователем
        if extra_fields.get('is_superuser'):
            user = self.model(
                username=username,
                **extra_fields
            )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(username=username, email=email, password=password, **extra_fields)

    def create_superuser(self, username, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(
            username=username,
            password=password,
            **extra_fields
        )


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(_('Имя пользователя'), max_length=255, unique=True)
    email = models.EmailField(_('Email'), null=True, blank=True)
    phone = models.CharField('Телефон', max_length=15, default='', blank=True)
    is_active = models.BooleanField(_('Активен'), default=False)
    is_staff = models.BooleanField(_('Персонал'), default=False)
    is_verified = models.BooleanField(_('Верификация'), default=False)
    date_joined = models.DateTimeField(_('Дата создания'), auto_now_add=True)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    class Meta:
        verbose_name = _('Пользователь')
        verbose_name_plural = _('Список пользователей')
        unique_together = ('username', 'email', 'phone')

    def __str__(self):
        return f"{self.email}"
