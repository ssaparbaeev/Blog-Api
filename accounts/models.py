from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class CustomUserModel(AbstractUser):
    name = models.CharField(null=True, blank=True, max_length=150)

    def __str__(self) -> str:
        return self.email
