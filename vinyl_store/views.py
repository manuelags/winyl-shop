from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Vinyl, Artist, Genre

class VinylListView(ListView):
    model = Vinyl
    template_name = 'vinyl_store/vinyl_list.html'
    context_object_name = 'vinyls'

class VinylDetailView(DetailView):
    model = Vinyl
    template_name = 'vinyl_store/vinyl_detail.html'

class ArtistListView(ListView):
    model = Artist
    template_name = 'vinyl_store/artist_list.html'
    context_object_name = 'artists'

def genre_products(request, genre_id):
    genre = get_object_or_404(Genre, id=genre_id)
    vinyls = Vinyl.objects.filter(genre=genre)
    return render(request, 'vinyl_store/genre_products.html', {
        'genre': genre,
        'vinyls': vinyls
    })
