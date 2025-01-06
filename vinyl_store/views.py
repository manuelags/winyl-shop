from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views.generic.dates import YearArchiveView, MonthArchiveView
from django.urls import reverse_lazy
from .models import Vinyl, Artist, Genre, Order
from django import forms

# List Views
class VinylListView(ListView):
    model = Vinyl
    template_name = 'vinyl_store/vinyl_list.html'
    context_object_name = 'vinyls'

class ArtistListView(ListView):
    model = Artist
    template_name = 'vinyl_store/artist_list.html'
    context_object_name = 'artists'

class GenreListView(ListView):
    model = Genre
    template_name = 'vinyl_store/genre_list.html'
    context_object_name = 'genres'

# Detail Views
class VinylDetailView(DetailView):
    model = Vinyl
    template_name = 'vinyl_store/vinyl_detail.html'

class ArtistDetailView(DetailView):
    model = Artist
    template_name = 'vinyl_store/artist_detail.html'

# Create, Update, Delete Views
class VinylCreateView(CreateView):
    model = Vinyl
    template_name = 'vinyl_store/vinyl_form.html'
    fields = ['title', 'artist', 'genre', 'price', 'description', 'release_date', 'stock']
    success_url = reverse_lazy('vinyl_store:vinyl-list')

    def get_form(self):
        form = super().get_form()
        form.fields['release_date'].widget = forms.DateInput(attrs={'type': 'date'})
        return form

class VinylUpdateView(UpdateView):
    model = Vinyl
    template_name = 'vinyl_store/vinyl_form.html'
    fields = ['title', 'artist', 'genre', 'price', 'description', 'release_date', 'stock']
    success_url = reverse_lazy('vinyl_store:vinyl-list')

    def get_form(self):
        form = super().get_form()
        form.fields['release_date'].widget = forms.DateInput(attrs={'type': 'date'})
        return form

class VinylDeleteView(DeleteView):
    model = Vinyl
    template_name = 'vinyl_store/vinyl_confirm_delete.html'
    success_url = reverse_lazy('vinyl_store:vinyl-list')

# Additional Views (as per requirements)
class OrderYearArchiveView(YearArchiveView):
    model = Order
    date_field = 'created_at'
    make_object_list = True
    template_name = 'vinyl_store/order_year_archive.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Oblicz łączną wartość zamówień
        total_value = sum(order.total_price for order in context['object_list'])
        context['total_value'] = total_value
        return context

class VinylsByGenreView(ListView):
    template_name = 'vinyl_store/vinyls_by_genre.html'
    context_object_name = 'vinyls'

    def get_queryset(self):
        return Vinyl.objects.filter(genre__id=self.kwargs['genre_id'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['genre'] = Genre.objects.get(id=self.kwargs['genre_id'])
        return context

class OrderListView(ListView):
    model = Order
    template_name = 'vinyl_store/order_list.html'
    context_object_name = 'orders'
    ordering = ['-created_at']  # Najnowsze pierwsze

class OrderDetailView(DetailView):
    model = Order
    template_name = 'vinyl_store/order_detail.html'
    context_object_name = 'order'

# Artist CRUD
class ArtistCreateView(CreateView):
    model = Artist
    template_name = 'vinyl_store/artist_form.html'
    fields = ['name', 'description']
    success_url = reverse_lazy('vinyl_store:artist-list')

class ArtistUpdateView(UpdateView):
    model = Artist
    template_name = 'vinyl_store/artist_form.html'
    fields = ['name', 'description']
    success_url = reverse_lazy('vinyl_store:artist-list')

class ArtistDeleteView(DeleteView):
    model = Artist
    template_name = 'vinyl_store/artist_confirm_delete.html'
    success_url = reverse_lazy('vinyl_store:artist-list')

# Genre CRUD
class GenreCreateView(CreateView):
    model = Genre
    template_name = 'vinyl_store/genre_form.html'
    fields = ['name']
    success_url = reverse_lazy('vinyl_store:genre-list')

class GenreUpdateView(UpdateView):
    model = Genre
    template_name = 'vinyl_store/genre_form.html'
    fields = ['name']
    success_url = reverse_lazy('vinyl_store:genre-list')

class GenreDeleteView(DeleteView):
    model = Genre
    template_name = 'vinyl_store/genre_confirm_delete.html'
    success_url = reverse_lazy('vinyl_store:genre-list')

# Order CRUD
class OrderCreateView(CreateView):
    model = Order
    template_name = 'vinyl_store/order_form.html'
    fields = ['vinyl', 'quantity', 'status']
    success_url = reverse_lazy('vinyl_store:order-list')

    def form_valid(self, form):
        order = form.save(commit=False)
        order.total_price = order.vinyl.price * order.quantity
        return super().form_valid(form)

class OrderUpdateView(UpdateView):
    model = Order
    template_name = 'vinyl_store/order_form.html'
    fields = ['vinyl', 'quantity', 'status']
    success_url = reverse_lazy('vinyl_store:order-list')

    def form_valid(self, form):
        order = form.save(commit=False)
        order.total_price = order.vinyl.price * order.quantity
        return super().form_valid(form)

class OrderDeleteView(DeleteView):
    model = Order
    template_name = 'vinyl_store/order_confirm_delete.html'
    success_url = reverse_lazy('vinyl_store:order-list')
