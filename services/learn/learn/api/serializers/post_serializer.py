from rest_framework import serializers

class PostSerializer(serializers.Serializer):
    id = serializers.CharField()
    name = serializers.CharField()
