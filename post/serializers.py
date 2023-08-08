from rest_framework import serializers
from .models import *


class PostSerializer(serializers.ModelSerializer):
    comments = serializers.SerializerMethodField(read_only=True)
    like_cnt = serializers.IntegerField(read_only=True)

    def get_comments(self, instance):
        serializer = CommentSerializer(instance.comments, many=True)
        return serializer.data
    
    class Meta:
        model = Post
        fields = '__all__'
        read_only_field = [
            "id", 
            "created_at",
            "updated_at",
            "comments",
        ]


class PostListSerializer(serializers.ModelSerializer):
    comments_cnt = serializers.SerializerMethodField()
    like_cnt = serializers.IntegerField()

    def get_comments_cnt(self, instance):
        return instance.comments.count()
    
    class Meta:
        model = Post
        fields = [
            "id",
            "created_at",
            "updated_at",
            "comments_cnt",
            "like_cnt",
        ]
        read_only_fields = ["id", "created_at", "updated_at", "comments_cnt"]


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ['post']