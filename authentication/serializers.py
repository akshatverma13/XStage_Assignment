from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'favorite_genres', 'watched_anime']
        extra_kwargs = {
            'favorite_genres': {'required': False},
            'watched_anime': {'required': False}
        }

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email', ''),
            password=validated_data['password']
        )
        user.favorite_genres = validated_data.get('favorite_genres', [])
        user.watched_anime = validated_data.get('watched_anime', [])
        user.save()
        return user

class UserPreferencesSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['favorite_genres', 'watched_anime']