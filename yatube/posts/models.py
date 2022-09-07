from pyexpat import model
from turtle import title
from django.db import models
from django.contrib.auth import get_user_model

Group =get_user_model()
User = get_user_model()

class Group(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL", null = True)
    description = models.TextField()

    def __str__(self) -> str:
        return self.title

class Post(models.Model):
    text = models.TextField()
    pub_date = models.DateTimeField('дата публикации', auto_now_add = True)
    author = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'posts') 
    group = models.ForeignKey(Group, on_delete = models.CASCADE, blank = True, null = True)

