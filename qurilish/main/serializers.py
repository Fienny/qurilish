from rest_framework import serializers
from .models import *


class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = "__all__"


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = "__all__"


class NewSerializer(serializers.ModelSerializer):
    class Meta:
        model = New
        fields = "__all__"


class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = "__all__"


class SystemSerializer(serializers.ModelSerializer):
    class Meta:
        model = System
        fields = "__all__"
        depth = 4


class SubsystemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subsystem
        fields = "__all__"
        depth = 3


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = "__all__"
        depth = 2


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        exclude = ['likes', 'dislikes']
