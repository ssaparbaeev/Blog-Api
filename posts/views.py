from django.shortcuts import render
from rest_framework import generics
from .models import PostModel
from .serializers import PostModelSerializer


# Create your views here.
class PostListView(generics.ListCreateAPIView):
    queryset = PostModel.objects.all()
    serializer_class = PostModelSerializer


class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PostModel.objects.all()
    serializer_class = PostModelSerializer
