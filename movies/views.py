from django.shortcuts import render, redirect
from .forms import MovieForm

# Create your views here.
def index(request):
    return render(request, 'index.html')

def create(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            movie = form.save(commit=False)
            movie.user = request.user
            movie.save()
            return redirect('movies:detail', movie.pk)
    else:
        form = MovieForm()
    context = {
        'form': form,
    }
    return render(request, 'movies/create.html', context)

def detail(reqeust, movie_pk):
    pass