from datetime import timezone
from django.utils import timezone
from django.views import generic
from .models import Post
from django.shortcuts import render ,redirect
# Create your views here.
class PostDetailView(generic.DetailView):
    template_name = "posts/detailes.html"
    context_object_name = "post"
    model = Post # we defined model here and set the value of post to tell Jquery which model it should retrive a single object from when use pk in the url

class PostListView(generic.ListView):
    template_name = "posts/index.html"
    context_object_name = "posts"
    def get_queryset(self):
        return Post.objects.filter(user_id=self.request.user)

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
