from django.contrib.auth import get_user_model
from rest_framework import viewsets
from .models import PostModel
from .serializers import PostModelSerializer, UserModelSerializer
from rest_framework.permissions import IsAdminUser
from .permissions import IsAuthorOrReadOnly


# Create your views here.
class PostViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = PostModel.objects.all()
    serializer_class = PostModelSerializer


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAdminUser,)
    queryset = get_user_model().objects.all()
    serializer_class = UserModelSerializer
