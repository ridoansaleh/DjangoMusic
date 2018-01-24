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