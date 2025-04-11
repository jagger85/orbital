from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django.core.exceptions import ValidationError

# Create your models here.


class Role(models.TextChoices):
    ADMIN = 'admin', 'Admin'
    USER = 'user', 'User'
    GUEST = 'guest', 'Guest'


class User(AbstractUser):
    email = models.EmailField(unique=True, blank=False)
    role = models.CharField(
        max_length=10, choices=Role.choices, default=Role.USER)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def clean(self):
        super().clean()
        if not self.email:
            raise ValidationError({'email': 'Email is required.'})

    def __str__(self):
        return self.username
