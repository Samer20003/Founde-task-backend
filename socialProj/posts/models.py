from django.db import models

# Create your models here.
class Post(models.Model):
    body = models.CharField(max_length=200)
    img_url = models.CharField(max_length=200)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    pup_date = models.DateTimeField()

class Comment(models.Model):
    body = models.CharField(max_length=200)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
