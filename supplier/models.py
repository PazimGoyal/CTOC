from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Supplier(models.Model):
    name = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name.username
