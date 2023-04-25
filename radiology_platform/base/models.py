from django.db import models
from bs4 import BeautifulSoup

# Create your models here.


class Post(models.Model):
    title=models.CharField(max_length=255)
    # models.CASCADE if we delete a user all the instances of posts created with him will be deleted 
   
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
class Subscribers(models.Model):
    name=models.CharField(max_length=50, null=True)
    email=models.EmailField(null=True)
    date= models.DateTimeField(auto_now_add=True)   
    def __str__(self):
        return self.email
    def __str__(self):
        return self.name
class MailMessage(models.Model) :
    title = models.CharField(max_length=100,null=True)  
    message=models.TextField(null=True)
    def __str__(self):
        return self.title
    def __str__(self):
        return self.message