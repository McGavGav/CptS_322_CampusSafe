from django.db import models


# Create your models here.
class User(models.Model):
    user_id = models.CharField(max_length=8, unique=True)
    last_name = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.user_id})"
