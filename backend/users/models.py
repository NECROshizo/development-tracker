from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    """Класс переопределяет стандартную модель User."""

    email = models.EmailField(
        verbose_name=_("Адрес электронной почты"),
        unique=True,
        blank=False,
        error_messages={
            'unique': _('Пользователь с таким email уже существует')
        },
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    class Meta:
        ordering = ['id']
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.email
