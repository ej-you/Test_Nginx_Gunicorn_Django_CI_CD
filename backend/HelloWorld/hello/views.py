from rest_framework import status
from django.shortcuts import render

from .models import CiCdUser

# Create your views here.


def index(request):
    data = {
        "title": "Index",
        "body": 'INDEX',
    }

    return render(request, 'index.html', context=data, status=status.HTTP_200_OK)


def hello_world(request):
    data = {
        "title": "Hello world",
        "body": 'Hello world',
    }

    return render(request, 'index.html', context=data, status=status.HTTP_200_OK)


def users(request):
    user_queryset = CiCdUser.objects.all()

    user_list = [
        {
            "email": user.email,
            "password": user.password,
            "bio": bio if (bio := user.bio) else "!!!Doesn't exist!!!",
        }
        for user in user_queryset
    ]

    data = {
        "title": "Users",
        "body": user_list,
    }

    return render(request, 'index.html', context=data, status=status.HTTP_200_OK)


# insert into ci_cd_users (email, password, bio) VALUES
# ('ejyou.user@gmail.com', '123qwerty', 'about me'),
# ('test@test.com', 'password', 'nothing'),
# ('sample@sample.ru', 'easy_pass', NULL);
