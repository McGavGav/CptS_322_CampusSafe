from django.db import models


# Create your models here.
class User(models.Model):
    user_id = models.CharField(max_length=8, unique=True)
    last_name = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.user_id})"

class EmergencyAlert(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    status = models.CharField(max_length=20)
    timestamp = models.DateTimeField(auto_now_add=True)
    latitude = models.CharField(max_length=30, null=True, blank=True)
    longitude = models.CharField(max_length=30, null=True, blank=True)

    def __str__(self):
        return f"{self.user} - {self.status}"