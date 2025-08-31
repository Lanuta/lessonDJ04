from django.shortcuts import render, redirect
from .models import Film
from .forms import FilmForm

# Страница с формой добавления фильма
def add_film(request):
    if request.method == "POST":
        form = FilmForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('film_list')
    else:
        form = FilmForm()
    return render(request, 'films/add_film.html', {'form': form})

# Страница со списком фильмов
def film_list(request):
    films = Film.objects.all()
    return render(request, 'films/film_list.html', {'films': films})

# Главная страница
def home(request):
    return render(request, 'films/home.html')

# Страница фильма
def film_detail(request, film_id):
    context = {'film_id': film_id}
    return render(request, 'films/film_detail.html', context)

