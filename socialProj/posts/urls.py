from tkinter.font import names

from django.urls import  path
from . import views
app_name = "posts"
urlpatterns =[
    path("<int:pk>/", views.PostDetailView.as_view(), name="detail"),
    path("list_view/", views.PostListView.as_view(), name="list_view"),
    path("add/", views.add_post, name="add_post"),
    path("<int:pk>/delete/", views.delete_post, name="delete_post"),
    path("<int:pk>/edit/", views.edit_post, name="edit_post")
]