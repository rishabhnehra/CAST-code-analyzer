from django.db import models

from user.models import User

# Create your models here.
class Syntax(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tested_on = models.DateField(auto_now=False, auto_now_add=True)
    result = models.TextField()