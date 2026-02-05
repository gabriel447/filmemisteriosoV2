import os
import django
import sys

# Setup Django environment
sys.path.append('/Users/gabeecwb/Projects/meu_site')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'meu_site.settings')
django.setup()

from filmes.models import Movie, Genre, StreamingPlatform

print(f"Total Movies: {Movie.objects.count()}")
print(f"Total Genres: {Genre.objects.count()}")
print(f"Total Streams: {StreamingPlatform.objects.count()}")

print("\n--- Genres ---")
for g in Genre.objects.all():
    print(f"ID: {g.id}, Name: {g.name}")

print("\n--- Streams ---")
for s in StreamingPlatform.objects.all():
    print(f"ID: {s.id}, Name: {s.name}")

print("\n--- Movies ---")
for m in Movie.objects.all():
    streams = ", ".join([s.name for s in m.streams.all()])
    print(f"ID: {m.id}, Title: {m.title}, Rating: {m.rating}, Genre: {m.genre.name if m.genre else 'None'}, Streams: [{streams}]")
