from django.db import models
from login.models import User

# Create your models here.

class Poke(models.Model):
    id = models.AutoField(primary_key=True)
    emisor = models.ForeignKey(User,related_name='emisor_poke',on_delete=models.CASCADE)
    receptor = models.ForeignKey(User,related_name='receptor_poke',on_delete=models.CASCADE)