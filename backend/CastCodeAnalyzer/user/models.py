from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    added_on = models.DateField(auto_now=False, auto_now_add=True)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.name