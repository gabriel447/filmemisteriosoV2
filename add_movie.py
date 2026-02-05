import os
import django
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from filmes.models import Movie, Genre, StreamingPlatform

# Get instances
netflix = StreamingPlatform.objects.get(name__iexact="Netflix")
romance = Genre.objects.get(name__iexact="romance")

# Create movie
movie = Movie.objects.create(
    title="Diário de uma Paixão",
    description="Um jovem pobre se apaixona por uma rica herdeira, mas são separados pelas diferenças sociais e pela guerra.",
    rating=8.2,
    genre=romance
)
movie.streams.add(netflix)
movie.save()

print(f"Filme '{movie.title}' adicionado com sucesso para Netflix + Romance!")
