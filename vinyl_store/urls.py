from django.urls import path
from . import views

app_name = 'vinyl_store'

urlpatterns = [
    # Vinyl URLs
    path('', views.VinylListView.as_view(), name='vinyl-list'),
    path('vinyl/<int:pk>/', views.VinylDetailView.as_view(), name='vinyl-detail'),
    path('vinyl/<int:pk>/update/', views.VinylUpdateView.as_view(), name='vinyl-update'),
    path('vinyl/<int:pk>/delete/', views.VinylDeleteView.as_view(), name='vinyl-delete'),

    # Artist URLs
    path('artists/', views.ArtistListView.as_view(), name='artist-list'),
    path('artists/<int:pk>/', views.ArtistDetailView.as_view(), name='artist-detail'),

    # Additional URLs
    path('monthly-sales/', views.monthly_sales, name='monthly-sales'),
    path('genre/<int:genre_id>/products/', views.genre_products, name='genre-products'),
]