from django.urls import path
from . import views

urlpatterns = [
    # Define the URL pattern for your view
    path('all-cards/', views.PostListView.as_view(), name='all policy-cards'),
    path('comments/<int:post_id>/', views.PostCommentsView.as_view(), name='post-comments'),
    path('comments/<int:post_id>/add/', views.AddCommentToPostView.as_view(), name='add-comment-to-post'),
]
