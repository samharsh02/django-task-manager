from django.contrib.auth.models import AbstractUser #this class has all the default required entities for a user
from django.db import models

# User Roles required for our application
ROLE_CHOICES = [
    ("admin", "Admin"),
    ("manager", "Manager"),
    ("developer", "Developer"),
]

class CustomUser(AbstractUser):
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default="developer")

    def __str__(self):
        return self.username
