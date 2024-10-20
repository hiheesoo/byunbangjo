from django.shortcuts import render, redirect
from .models import Movie, Comment
from .forms import MovieForm, CommentForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    movies = Movie.objects.all()
    context = {
        'movies': movies
    }
    return render(request, 'index.html', context)

@login_required
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
    return render(request, 'create.html', context)

def detail(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    context = {
        'movie': movie
    }
    return render(request, 'detail.html', context)

@login_required
def likes(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    if request.user in movie.like_users.all():
        movie.like_users.remove(request.user)
    else:
        movie.like_users.add(request.user)
    return redirect('movies:index')

@login_required
def dislikes(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    if request.user in movie.dislike_users.all():
        movie.dislike_users.remove(request.user)
    else:
        movie.dislike_users.add(request.user)
    return redirect('movies:index')
  
@login_required
def update(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    if request.user == movie.user:
        if request.method == 'POST':
            form = MovieForm(request.POST, instance=movie)
            if form.is_valid():
                form.save()
                return redirect('movies:detail', movie.pk)
        else:
            form = MovieForm(instance=movie)
        context = {
            'movie': movie,
            'form': form,
        }

        return render(request, 'update.html', context)
    else:
        return redirect('movies:index')

@login_required
def delete(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    if request.user == movie.user:
        movie.delete()
    return redirect('movies:index')

def comments_create(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.movie = movie
        comment.user = request.user
        comment.save()
        return redirect('movies:detail', movie.pk)
    else:
        comment_form = CommentForm()
    context = {
        'comment_form': comment_form
    }
    return render(request, 'detail.html', context)

def comments_delete(request, movie_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    if request.user == comment.user:
        comment.delete()
    return redirect('movies:detail', movie_pk)

