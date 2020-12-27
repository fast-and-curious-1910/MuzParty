from django.db import models

# Create your models here.


class Room(models.Model):
    max_len = 8
    defcode = ''
    code = models.CharField(max_length=max_len, default=defcode, unique=True)
    host = models.CharField(max_length=20, unique=True)
