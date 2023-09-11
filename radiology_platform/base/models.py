from django.db import models
from bs4 import BeautifulSoup
from ckeditor.fields import RichTextField

from django.core.files.uploadedfile import InMemoryUploadedFile


class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255, null=True)
    body = RichTextField(blank=True, null=True)
    image = models.ImageField(upload_to="blog_images/", null=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-updated", "-created"]

    def get_short_description(self):
        body = self.body.strip()
        description = body[:50] + "..."
        return description

    def save(self, *args, **kwargs):
        self.title = self.title.upper()
        super(Post, self).save(*args, **kwargs)

    def update_image(self, image_file):
        if isinstance(image_file, InMemoryUploadedFile):
            self.image = image_file
            self.save()


class Subscribers(models.Model):
    name = models.CharField(max_length=50, null=True)
    email = models.EmailField(null=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email

    def __str__(self):
        return self.name
