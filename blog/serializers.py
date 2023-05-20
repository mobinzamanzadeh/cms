from rest_framework import serializers
from blog.models import Post, Comment, User, Tag
from rest_framework.authtoken.models import Token


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'is_staff', "is_superuser", 'is_active']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            email=validated_data['email'],
            is_staff=validated_data['is_staff'],
            is_superuser=validated_data['is_superuser'],
            is_active=validated_data['is_active'],
        )
        Token.objects.create(user=user)
        return user


class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    # tag = serializers.ReadOnlyField()
    # category = serializers.ReadOnlyField(source='category.name')

    class Meta:
        model = Post
        fields = ['id', 'title', 'slug', 'content', 'author', 'tag', 'category']

    def create(self, validated_data):
        validated_data['author'] = self.context['request'].user
        post = Post.objects.create(**validated_data)
        return post



