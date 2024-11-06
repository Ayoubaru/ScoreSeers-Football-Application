from django.db import models
from datetime import datetime


# Create your models here.


class Clients_msg(models.Model):
    email_contact_us = models.CharField(max_length=50, null=True)
    name_contact_us = models.CharField(max_length=50, null=True)
    message_contact_us = models.TextField(max_length=50, null=True)

    def __str__(self):
        return self.name_contact_us
    
class News(models.Model):
    news_title = models.CharField(max_length=100,null=False)
    news_text = models.TextField(max_length=10000, null=False)
    news_image = models.ImageField(upload_to='news_photos/%y/%m/%d')
    news_activate = models.BooleanField(default=False)

    def __str__(self):
        return self.news_title