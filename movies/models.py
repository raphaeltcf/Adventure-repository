from django.db import models
from users.models import User
# Create your models here.

class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    release_date = models.DateField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='movies')
    genre = models.CharField(max_length=100)
    rating = models.FloatField()
    duration = models.IntegerField()
    image = models.ImageField(upload_to='movies/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)