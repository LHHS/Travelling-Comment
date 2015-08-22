from django.db import models
from django import forms

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(blank=True)
    photo = models.URLField(blank=True)
    required_time = models.IntegerField()
    location = models.CharField(max_length=100)
    created_date = models.DateTimeField(auto_now_add=True)


class Block(models.Model):
    post = models.ForeignKey(Post)
    comment = models.TextField()
    photo = models.URLField()
    location = models.CharField(max_length=100)
    rating = models.DecimalField(max_digits=1, decimal_places=1)

class ContactForm(forms.Form):
    subject=forms.CharField(max_length=100)
    message=forms.CharField()
    sender=forms.EmailField()
    cc_myself=forms.BooleanField(required=False)
# Create your models here.
