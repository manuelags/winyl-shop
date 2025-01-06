from django.urls import path
from . import views

app_name = 'vinyl_store'

urlpatterns = [
    # List views
    path('', views.VinylListView.as_view(), name='vinyl-list'),
    path('artists/', views.ArtistListView.as_view(), name='artist-list'),
    path('genres/', views.GenreListView.as_view(), name='genre-list'),

    # Detail views
    path('vinyl/<int:pk>/', views.VinylDetailView.as_view(), name='vinyl-detail'),
    path('artist/<int:pk>/', views.ArtistDetailView.as_view(), name='artist-detail'),

    # Create, Update, Delete views
    path('vinyl/add/', views.VinylCreateView.as_view(), name='vinyl-add'),
    path('vinyl/<int:pk>/edit/', views.VinylUpdateView.as_view(), name='vinyl-edit'),
    path('vinyl/<int:pk>/delete/', views.VinylDeleteView.as_view(), name='vinyl-delete'),

    # Additional views
    path('orders/<int:year>/', views.OrderYearArchiveView.as_view(), name='order-year-archive'),
    path('genre/<int:genre_id>/vinyls/', views.VinylsByGenreView.as_view(), name='vinyls-by-genre'),
    path('orders/', views.OrderListView.as_view(), name='order-list'),
    path('order/<int:pk>/', views.OrderDetailView.as_view(), name='order-detail'),
]