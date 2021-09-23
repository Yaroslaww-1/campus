from rest_framework import serializers


class UserSerializer(serializers.Serializer):
    id = serializers.CharField()
    name = serializers.CharField()
    email = serializers.EmailField()


class UserCreateSerializer(serializers.Serializer):
    name = serializers.CharField()
    email = serializers.EmailField()
