from django.db import models

# Create your models here.

class AdvertisementItem(models.Model):
    image = models.ImageField(upload_to='carousel_images')
    caption = models.CharField(max_length=200, blank=True)


# class Card(models.Model):
#     title = models.CharField(max_length=100, default='Sample Card')
#     content = models.TextField(default='This is a sample card with some random content. You can customize it as needed.')
#     image = models.ImageField(upload_to='card_images', null=True, blank=True)
#     link = models.URLField(default='https://example.com')