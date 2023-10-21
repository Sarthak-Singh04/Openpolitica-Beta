from .models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from .serializers import *


class PostListView(APIView):
    def get(self, request):
        posts = Post.objects.all().order_by('-date_created')
        serializer = PostSerializer(posts, many=True)  # Use your serializer to serialize the data
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    
        