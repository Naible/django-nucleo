from rest_framework import serializers
from django.contrib.auth.models import User
from models import Post, Cuisine, Atmosphere, Restaurant, UserProfile


class UserSerializer(serializers.ModelSerializer):
    posts = serializers.HyperlinkedIdentityField(view_name='userpost-list', lookup_field='username')

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'posts', )


class PostSerializer(serializers.ModelSerializer):
    author = UserSerializer(required=False)

    def get_validation_exclusions(self, *args, **kwargs):
        # Need to exclude `user` since we'll add that later based off the request
        exclusions = super(PostSerializer, self).get_validation_exclusions(*args, **kwargs)
        return exclusions + ['author']

    class Meta:
        model = Post


class CuisineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cuisine


class AtmosphereSerializer(serializers.ModelSerializer):
    class Meta:
        model = Atmosphere


class RestaurantSerializer(serializers.ModelSerializer):
    cuisines = CuisineSerializer(many=True, read_only=True)
    atmospheres = AtmosphereSerializer(many=True, read_only=True)

    class Meta:
        model = Restaurant


class UserProfileSerializer(serializers.ModelSerializer):
    follows = UserSerializer(many=True, read_only=True)
    favorites = RestaurantSerializer(many=True, read_only=True)

    class Meta:
        model = UserProfile
