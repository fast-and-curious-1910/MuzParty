from django.db import models
import string
import random
# Create your models here.


class Room(models.Model):
    max_len = 8
    defcode = ''
    code = models.CharField(max_length=max_len, default=defcode, unique=True)
    host = models.CharField(max_length=20, unique=True)
    guest_can_pause = models.BooleanField(null=False,default=False)
    votes_to_skip = models.IntegerField(null=False,default=1)
    created_at = models.DateTimeField(auto_now_add=True)

def gen_unique_code():
    length = Room.max_len
    while True:
        code = ''.join(random.choice(string.ascii_uppercase,k=length))
        if Room.objects.filter(code=code).count() == 0:
            break 
    return code

