from django.urls import path
from . import views


urlpatterns = [
    path("all-cards/", views.PostListView.as_view(), name="all policy-cards"),
]
