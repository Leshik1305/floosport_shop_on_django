from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    image = models.ImageField(
        upload_to="users-images",
        blank=True,
        null=True,
        verbose_name="Аватар",
    )
    phone_number = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        db_table = "user"
        verbose_name = "Пользователя"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.username
