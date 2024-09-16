from django.views import generic
from .models import Post
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

