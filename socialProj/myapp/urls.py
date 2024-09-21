from tkinter.font import names

from django.urls import path, include, re_path
from . import views
urlpatterns = [
   path('', views.index, name="home"),
   path('login/', views.user_login, name="login"),
   path('signup/', views.user_signup, name="signup"),
   path('logout/', views.user_logout, name="logout"),
   path("userapi/", views.UserListCreate.as_view(), name="user-list-create"),
   path("userapi/<int:pk>/", views.UserRetrieveUpdateDestroy.as_view(),name="update"),
   re_path('login', views.login),
   re_path('signup', views.signup),
]