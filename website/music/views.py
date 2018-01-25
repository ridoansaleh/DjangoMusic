from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import SongForm
from .models import Song

def index(request):
    if request.method == 'POST':
        form = SongForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')

    else:
        form = SongForm()
    return render(request, 'music/index.html', {'form': form, 'songs': Song.objects.all() })

def edit(request, pk):
    _song = Song.objects.get(pk=pk)
    if request.method == 'POST':
        _song.title = request.POST['title']
        _song.genre = request.POST['genre']
        _song.singer = request.POST['singer']
        _song.rating = request.POST['rating']
        _song.save()
        return HttpResponseRedirect('/')

    return render(request, 'music/edit.html', {'song': _song })

def delete(request, pk):
    _song = Song.objects.get(pk=pk)
    _song.delete()
    return HttpResponseRedirect('/')