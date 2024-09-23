from datetime import timezone

from django.core.serializers import serialize
from django.utils import timezone
from django.views import generic
from .models import Post
from django.shortcuts import render ,redirect , get_object_or_404
from .form import PostForm
from rest_framework.decorators import api_view ,permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .seriallizers import PostSerializer, CreatePostSerializer , UpdatePostSerializer
from rest_framework import generics
# Create your views here.
class PostDetailView(generic.DetailView):
    template_name = "posts/detailes.html"
    context_object_name = "post"
    model = Post # we defined model here and set the value of post to tell Jquery which model it should retrive a single object from when use pk in the url

class PostListView(generic.ListView):
    template_name = "posts/index.html"
    context_object_name = "posts"
    def get_queryset(self):
        return Post.objects.filter(user_id=self.request.user) # ORM

def add_post (request):
    if request.method == "POST":
        body = request.POST.get('body')
        img_url = request.POST.get('img_url')
        user= request.user
        pup_date = timezone.now()

        new_post = Post(
            body = body,
            img_url = img_url,
            user_id = user,
            pup_date = pup_date
        )
        new_post.save()

        return redirect('posts:list_view')

    return redirect('posts:list_view')

def delete_post (requset, pk):
    post = get_object_or_404(Post, pk=pk)
    if requset.method == "POST":
        post.delete()
        return redirect('posts:list_view')
    return redirect(requset.META.get('HTTP_REFERER','posts:list_view')) # request.META is and dictionary in django that contain the HTTP headers sent with the requset , from it there is .get(HTTP_REFERER) and that will be the url of the previous page so we can redicrct the user in the same page and if it is empty for some reason the git methode will redirect to the path we put it

def edit_post (requset, pk):
    post = get_object_or_404(Post, pk=pk)
    if requset.method == 'POST':
        form = PostForm(requset.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('posts:list_view')
    else:
        form = PostForm(instance=post)
    return render(requset,'posts/edit_post.html',{'form':form})

@api_view(['GET'])
def post_list_view(request):
    posts = Post.objects.all()
    serializer = PostSerializer(posts, many=True) # the use of {many= True}: to serilaze a query set of objects which is a list of posts
    return Response(serializer.data)

@api_view (['DELETE'])
def post_delete(request, pk):
    try:
        post_obj= Post.objects.get(pk=pk)
        post_obj.delete()
        return Response({'msg': 'Post deleted successfully'}, status = status.HTTP_204_NO_CONTENT)
    except Post.DoesNotExist:
        return Response({'msg': 'Post not found'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def add_post(request):
    item = CreatePostSerializer(data=request.data)
    if item.is_valid():
        item.save()
        return Response(item.data, status=status.HTTP_201_CREATED)
    else:
        print(item.errors)
        return Response(item.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view (['PUT'])
def edit_post(request, pk):
    post = get_object_or_404(Post,pk=pk)
    serializer = UpdatePostSerializer(post,data= request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"msg":"post update sucssfully","post":serializer.data},status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

