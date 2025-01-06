from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.db.models import Sum
from datetime import datetime
from .models import Vinyl, Artist, Genre, Order

# Vinyl Views
class VinylListView(ListView):
    model = Vinyl
    template_name = 'vinyl_store/vinyl_list.html'
    context_object_name = 'vinyls'

class VinylDetailView(DetailView):
    model = Vinyl
    template_name = 'vinyl_store/vinyl_detail.html'

class VinylUpdateView(UpdateView):
    model = Vinyl
    template_name = 'vinyl_store/vinyl_form.html'
    fields = ['title', 'artist', 'genre', 'release_year', 'price', 'stock', 'description']
    success_url = reverse_lazy('vinyl-list')

class VinylDeleteView(DeleteView):
    model = Vinyl
    template_name = 'vinyl_store/vinyl_confirm_delete.html'
    success_url = reverse_lazy('vinyl-list')

# Artist Views
class ArtistListView(ListView):
    model = Artist
    template_name = 'vinyl_store/artist_list.html'
    context_object_name = 'artists'

class ArtistDetailView(DetailView):
    model = Artist
    template_name = 'vinyl_store/artist_detail.html'

# Additional Views
def monthly_sales(request):
    current_month = datetime.now().month
    current_year = datetime.now().year

    monthly_orders = Order.objects.filter(
        order_date__year=current_year,
        order_date__month=current_month,
        status='completed'
    )

    total_sales = monthly_orders.aggregate(Sum('total_price'))['total_price__sum'] or 0

    return render(request, 'vinyl_store/monthly_sales.html', {
        'orders': monthly_orders,
        'total_sales': total_sales,
        'month': current_month,
        'year': current_year
    })

def genre_products(request, genre_id):
    genre = get_object_or_404(Genre, id=genre_id)
    vinyls = Vinyl.objects.filter(genre=genre)

    return render(request, 'vinyl_store/genre_products.html', {
        'genre': genre,
        'vinyls': vinyls
    })
