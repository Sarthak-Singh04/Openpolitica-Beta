from rest_framework import serializers
from .models import Policy, Comment, UserVote

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

  # Import the Policy model from your app

class PolicySerializer(serializers.ModelSerializer):
    class Meta:
        model = Policy
        fields = ['policy_id', 'title', 'description', 'impact', 'cost', 'timeframe']


class UserVoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserVote
        fields = '__all__'

