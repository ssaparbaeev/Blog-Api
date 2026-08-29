from django.shortcuts import render
from rest_framework import generics
from .models import PostModel
from .serializers import PostModelSerializer
from .permissions import IsAuthorOrReadOnly


# Create your views here.
class PostListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = PostModel.objects.all()
    serializer_class = PostModelSerializer


class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = PostModel.objects.all()
    serializer_class = PostModelSerializer
