from django.shortcuts import render, get_object_or_404
from django.contrib.auth import login, authenticate
from django.http import HttpResponseRedirect
from .forms import SongForm, SignUpForm
from .models import Song

def home(request):
    status = ''
    if request.method == 'POST':
        form = SongForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('home')
    else:
        form = SongForm()
    # put render outside 'else' block, so user can see the error messages
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
    return HttpResponseRedirect('home')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.profile.birthdate = form.cleaned_data.get('birthdate')
            user.profile.gender = form.cleaned_data.get('gender')
            user.profile.address = form.cleaned_data.get('address')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return render(request, 'music/login.html', { })
    else:
        form = SignUpForm()
    return render(request, 'music/signup.html', { 'form': form })




