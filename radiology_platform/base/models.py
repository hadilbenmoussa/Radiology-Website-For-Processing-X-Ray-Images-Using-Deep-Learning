from django.db import models
from django.contrib.auth.models import User
from bs4 import BeautifulSoup

# Create your models here.

class Post(models.Model):
    title=models.CharField(max_length=255)
    # models.CASCADE if we delete a user all the instances of posts created with him will be deleted 
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    body=models.TextField()
        # when the model is updated
    updated = models.DateTimeField(auto_now=True)
    # when the room was created
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created']
    def __str__(self):
        return self.title + '|' + str(self.author)
    def get_short_description(self):
        body = self.body.strip()
    # Use string manipulation to extract the first 50 characters of the body
        description = body[:50] + '...'
        return description
    def save(self, *args, **kwargs):
        self.title = self.title.upper()
        super(Post, self).save(*args, **kwargs)