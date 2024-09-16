from django.db import models

# Create your models here.
class Post(models.Model):
    body = models.CharField(max_length=200)
    img_url = models.CharField(max_length=200)
    user_id = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    pup_date = models.DateTimeField()