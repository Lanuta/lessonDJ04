from django.urls import path
from . import views

urlpatterns = [
    path('', views.film_list, name='film_list'),          # список фильмов
    path('add/', views.add_film, name='add_film'),       # <-- добавление фильма
    path('<int:film_id>/', views.film_detail, name='film_detail'),
]