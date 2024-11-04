from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Article(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name = 'articles')
    title = models.CharField(max_length = 100)
    content = models.TextField()
    published_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return str(f"{self.author} {self.title}")
