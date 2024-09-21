from django.core.serializers import serialize
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from .serializers import UserSerializer
from django.contrib.auth.models import User
from .forms import SignupForm, LoginForm
from rest_framework import generics


# Create your views here.
# Home page
def index(request):
    return render(request, 'myapp/index.html')

# signup page
def user_signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignupForm()
    return render(request, 'myapp/signup.html', {'form': form})

# login page
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return  redirect('posts:list_view')
    else:
        form = LoginForm()
    return render(request, 'myapp/login.html', {'form': form})

# logout
def user_logout(request):
    logout(request)
    return redirect('login')

class UserListCreate(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = "pk"



# Login api
@api_view(['POST'])
def login(request):
    user = get_object_or_404(User, username= request.data['username'])
    if not user.check_password(request.data['password']):
        return Response({"detail": "Not found."}, status=status.HTTP_400_BAD_REQUEST)
    token, created = Token.objects.get_or_create(user=user)
    serializer = UserSerializer(instance=user)
    return Response({"token": token.key, "user": serializer.data})


@api_view(['POST'])
def signup(request):
    serializer = UserSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        user = User.objects.get(username = request.data['username'])
        user.set_password(request.data['password'])
        user.save()
        token = Token.objects.create(user = user)
        return Response ({"token": token.key, "user": serializer.data})
    return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)