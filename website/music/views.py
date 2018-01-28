from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .forms import SongForm
from .models import Song

def index(request):
    status = ''
    if request.method == 'POST':
        form = SongForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = SongForm()
        return render(request, 'music/index.html', {'form': form, 'songs': Song.objects.all(), 'status': status })

def edit(request, pk):
    song = get_object_or_404(Song, pk=pk)
    status = 'success'
    titleValue = Song.objects.filter(pk=pk).values('title')[0];
    song_title = titleValue['title']
    
    if request.method == 'POST':
        post_form = SongForm(request.POST, instance=song)
        if post_form.is_valid():
            post_form.save()
            return render(request, 'music/edit.html', {'form': post_form, 'status': status, 'song_title': song_title })
    else:
        form = SongForm(instance=song)
        return render(request, 'music/edit.html', {'form': form, 'song_title': song_title })

def delete(request, pk):
    song = Song.objects.get(pk=pk)
    song.delete()
    return HttpResponseRedirect('/')