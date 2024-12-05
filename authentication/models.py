from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    favorite_genres = models.JSONField(default=list, blank=True)
    watched_anime = models.JSONField(default=list, blank=True)