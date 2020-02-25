from django.db import models


class Users(models.Model):
    first_name = models.CharField(max_length=264, unique=True)
    last_name = models.CharField(max_length=264, unique=True)
    email = models.EmailField(max_length=264, unique=True)

