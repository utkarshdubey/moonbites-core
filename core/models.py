from django.db import models
import datetime

class Post(models.Model):
  title = models.TextField()
  author_name = models.TextField()
  author_website = models.TextField()
  short_description = models.TextField()
  content = models.TextField()
  genre = models.TextField(default='Poem')
  created_on = models.DateTimeField(auto_now_add=True)
  def __str__(self):
    return self.title