from tkinter.font import names

from django.urls import  path, re_path
from . import views
app_name = "posts"
urlpatterns =[
    path("<int:pk>/", views.PostDetailView.as_view(), name="detail"),
    path("list_view/", views.PostListView.as_view(), name="list_view"),
    path("<int:pk>/delete/", views.delete_post, name="delete_post"),
    path("<int:pk>/edit/", views.edit_post, name="edit_post"),
    path('post_list_view', views.post_list_view, name='post_list_view'),
    path('delete_post/<int:pk>/', views.post_delete, name='post_delete'),
    path('add_post', views.add_post, name="add_post"),
    path('edit_post/<int:pk>/', views.edit_post, name="edit_post")

]