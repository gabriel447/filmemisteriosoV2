from rest_framework import serializers
from .models import StreamingPlatform, Genre, Movie
import base64
import uuid
from django.core.files.base import ContentFile

class Base64ImageField(serializers.ImageField):
    def to_internal_value(self, data):
        if isinstance(data, str) and data.startswith('data:image'):
            # format: "data:image/png;base64,..."
            format, imgstr = data.split(';base64,')
            ext = format.split('/')[-1]
            id = uuid.uuid4()
            data = ContentFile(base64.b64decode(imgstr), name=f"{id}.{ext}")
        return super().to_internal_value(data)

class StreamingPlatformSerializer(serializers.ModelSerializer):
    icon = Base64ImageField(required=False, allow_null=True)
    
    class Meta:
        model = StreamingPlatform
        fields = '__all__'

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'

class MovieSerializer(serializers.ModelSerializer):
    image = Base64ImageField(required=False, allow_null=True)
    streams = StreamingPlatformSerializer(many=True, read_only=True)
    stream_ids = serializers.PrimaryKeyRelatedField(
        queryset=StreamingPlatform.objects.all(), 
        many=True, 
        write_only=True, 
        source='streams'
    )
    genre_name = serializers.CharField(source='genre.name', read_only=True)
    
    class Meta:
        model = Movie
        fields = ['id', 'title', 'description', 'image', 'rating', 'genre', 'genre_name', 'streams', 'stream_ids']
