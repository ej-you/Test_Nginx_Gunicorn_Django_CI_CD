from rest_framework import status
from rest_framework.response import Response

# Create your views here.


def index(request):
    return Response(data='<h1>INDEX</h1>', status=status.HTTP_200_OK)


def hello_world(request):
    return Response(data='Hello world!', status=status.HTTP_200_OK)


def users(request):
    data = {
        "user1": 'user1',
    }
    return Response(data=data, status=status.HTTP_200_OK)
