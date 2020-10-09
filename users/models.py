from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """Custom User Model"""

    GENDER = (
        ('MALE', 'Male'),
        ('FEMALE', 'Female'),
        ('OTHER', 'other')
    )

    LANGUAGE = (
        ('ENGLISH', 'English'),
        ('RUSSIAN', 'Russian')
    )

    CURRENCY = (
        ('usd', 'USD'),
        ('rub', 'RUB')
    )

    avatar = models.ImageField(blank=True)
    gender = models.CharField(max_length=10, choices=GENDER)
    bio = models.TextField(default='', blank=True)
    birthdate = models.DateField(blank=True, null=True)
    language = models.CharField(max_length=20, choices=LANGUAGE, blank=True)
    currency = models.CharField(max_length=3, choices=CURRENCY, blank=True)
    superhost = models.BooleanField(default=False)
