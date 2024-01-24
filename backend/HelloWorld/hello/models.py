from django.db import models


class CiCdUser(models.Model):
    email = models.EmailField(max_length=150, null=False, blank=False)
    password = models.CharField(max_length=255, null=False, blank=False)
    bio = models.TextField(null=True)
