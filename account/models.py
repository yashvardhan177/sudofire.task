from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class UserMod(User):
    mobile_num = models.IntegerField(unique=True, max_length=10)


class Customer(models.Model):
    profile_number = models.IntegerField(primary_key=True, auto_created=True)
    user = models.OneToOneField(UserMod, on_delete=models.CASCADE)
