from rest_framework import serializers
from .models import Post
from myapp.serializers import UserSerializer
class PostSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Post
        fields = ["id","body","img_url","user",'pup_date']

class CreatePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ["body", "img_url", "user",'pup_date']

class UpdatePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ["body", "img_url","id"]
