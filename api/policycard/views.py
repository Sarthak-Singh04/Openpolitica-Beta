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

    def post(self, request):
        serialized_post = PostSerializer(data=request.data)
        if serialized_post.is_valid():
            serialized_post.save()
            return Response(serialized_post.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serialized_post.errors, status=status.HTTP_400_BAD_REQUEST)
        
        
        
class PostCommentsView(APIView):
    def get(self, request, post_id):
        comments = Comment.objects.filter(post_id=post_id).order_by('-date_created')
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    


class AddCommentToPostView(APIView):
    def post(self, request, post_id):
        # Find the specific post
        post = get_object_or_404(Post, id=post_id)
        
        # Create the comment and associate it with the post
        serialized_comment = CommentSerializer(data=request.data)
        if serialized_comment.is_valid():
            comment = serialized_comment.save(post=post, author=request.user)
            
            # Redirect to the specific post after adding the comment
            return redirect('post-comments', post_id=post.id)
        else:
            return Response(serialized_comment.errors, status=status.HTTP_400_BAD_REQUEST)
        