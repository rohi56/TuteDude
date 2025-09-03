from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from helloworld.serializers import PostSerializer
from rest_framework.viewsets import ModelViewSet
from helloworld.models import Post
from rest_framework.permissions import IsAuthenticated
from helloworld.permissions import IsPostPossessor
from rest_framework import filters
from helloworld.filters import PostFilter
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.


class HelloWorldView(APIView):
    def get(self, request):
        return Response({'message': 'Hello, World!'})
    
class PostViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated, IsPostPossessor]
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [DjangoFilterBackend , filters.SearchFilter, filters.OrderingFilter]
    ordering_fields = ['id']
    filterset_class = PostFilter
    search_fields = ['title', 'content']
    
    def get_queryset(self):
        return Post.objects.filter(created_by=self.request.user)
    
 