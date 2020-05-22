from rest_framework import serializers
from bugtracker.models import App, Bug, Comment, Reply
from django.contrib.auth.models import User


class AppSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    bugs = serializers.HyperlinkedRelatedField(many=True, view_name='bug-detail', read_only=True)

    class Meta:
        model = App
        fields = ['url', 'created', 'id', 'name', 'up_for_testing',
                  'description', 'testing_instructions', 'owner', 'bugs', 'team_members']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    apps_owned = serializers.HyperlinkedRelatedField(many=True, view_name='app-detail', read_only=True)
    apps_member = serializers.HyperlinkedRelatedField(many=True, view_name='app-detail', read_only=True)

    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'apps_owned', 'apps_member']
        


class BugSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    comments = serializers.HyperlinkedRelatedField(many=True, view_name='comment-detail', read_only=True)

    class Meta:
        model = Bug
        fields = ['url', 'id', 'created', 'heading', 'app', 'owner', 'assigned_to', 'description', 'tag', 'is_resolved', 'comments']


class CommentSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    replies = serializers.HyperlinkedRelatedField(many=True, view_name='reply-detail', read_only=True)

    class Meta:
        model = Comment
        fields = ['url', 'id', 'created', 'owner', 'bug', 'content','replies']


class ReplySerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Reply
        fields = ['url', 'id', 'created', 'owner', 'comment', 'content']