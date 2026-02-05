from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render
from .models import StreamingPlatform, Genre, Movie
from .serializers import StreamingPlatformSerializer, GenreSerializer, MovieSerializer
import random

def index(request):
    return render(request, 'filmes/index.html')

class StreamingPlatformViewSet(viewsets.ModelViewSet):
    queryset = StreamingPlatform.objects.all()
    serializer_class = StreamingPlatformSerializer

class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def create(self, request, *args, **kwargs):
        if isinstance(request.data, list):
            serializer = self.get_serializer(data=request.data, many=True)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return super().create(request, *args, **kwargs)

@api_view(['GET'])
def recommend_movie(request):
    stream_id = request.query_params.get('stream_id')
    genre_id = request.query_params.get('genre_id')
    
    if not stream_id or not genre_id:
        return Response(
            {"error": "Por favor, forneça stream_id e genre_id"}, 
            status=status.HTTP_400_BAD_REQUEST
        )
        
    movies = Movie.objects.filter(
        streams__id=stream_id,
        genre__id=genre_id,
        rating__gt=8
    )
    
    if not movies.exists():
        return Response(
            {"message": "Nenhum filme 'nata' (>8.0) encontrado para essa combinação."}, 
            status=status.HTTP_404_NOT_FOUND
        )
        
    movie = random.choice(list(movies))
    serializer = MovieSerializer(movie)
    return Response(serializer.data)
