from django.shortcuts import render
import json

from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view


from serializers import UserSerializer, PostSerializer
from django.contrib.auth.models import User
from models import Post
from permissions import PostAuthorCanEditPermission


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [
        permissions.AllowAny
    ]


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'username'


class PostMixin(object):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [
        PostAuthorCanEditPermission
    ]

    def pre_save(self, obj):
        """Force author to the current user on save"""
        obj.author = self.request.user
        return super(PostMixin, self).pre_save(obj)


class PostList(PostMixin, generics.ListCreateAPIView):
    pass


class PostDetail(PostMixin, generics.RetrieveUpdateDestroyAPIView):
    pass


class UserPostList(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_queryset(self):
        queryset = super(UserPostList, self).get_queryset()
        return queryset.filter(author__username=self.kwargs.get('username'))


@api_view(['POST'])
def add_post(request):
    # POST request handler
    if request.method == 'POST':
        data = json.loads(request.body)
        print(repr(request.body))
        print(data['text'])

        author = User.objects.get(username=data['author'])

        post = Post(
            text=data['text'],
            author=author)
        post.save()

        return Response(status=status.HTTP_201_CREATED)