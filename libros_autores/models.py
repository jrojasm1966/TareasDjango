from django.db import models
import re
import bcrypt
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField

# Create your models here.

class books(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    desc = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class authors(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    notas = models.CharField(max_length=255,default='sin notas')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class books_authors(models.Model):
    book_id = models.IntegerField()
    author_id = models.IntegerField()

