from django.urls import path
from . import views

app_name = 'vinyl_store'

urlpatterns = [
    path('', views.VinylListView.as_view(), name='vinyl-list'),
    path('vinyl/<int:pk>/', views.VinylDetailView.as_view(), name='vinyl-detail'),
    path('artists/', views.ArtistListView.as_view(), name='artist-list'),
    path('genre/<int:genre_id>/products/', views.genre_products, name='genre-products'),
]