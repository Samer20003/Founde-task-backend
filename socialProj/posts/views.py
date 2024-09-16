from datetime import timezone
from django.utils import timezone
from django.views import generic
from .models import Post
from django.shortcuts import render ,redirect , get_object_or_404
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

def delete_post (requset, pk):
    post = get_object_or_404(Post, pk=pk)
    if requset.method == "POST":
        post.delete()
        return redirect('posts:list_view')
    return redirect(requset.META.get('HTTP_REFERER','posts:list_view')) # request.META is and dictionary in django that contain the HTTP headers sent with the requset , from it there is .get(HTTP_REFERER) and that will be the url of the previous page so we can redicrct the user in the same page and if it is empty for some reason the git methode will redirect to the path we put it
