from django.contrib import admin
from django.urls import path, include
from films import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),          # главная страница сайта
    path('films/', include('films.urls')),      # все страницы приложения films
]

