from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Profile, Album
from .forms import ProfileForm, AddAlbumForm, EditAlbumForm, DeleteAlbumForm


def get_profile():
    try:
        return Profile.objects.get()
    except Profile.DoesNotExist:
        return None


def index(request):
    profile = get_profile()

    if profile is None:
        if request.method == 'GET':
            form = ProfileForm()
        else:
            form = ProfileForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('home')

        context = {
            'form': form,
        }

        return render(request, 'core/home-no-profile.html', context)

    context = {
        'albums': Album.objects.all(),
    }

    return render(request, 'core/home-with-profile.html', context)


def add_album(request):
    if request.method == 'GET':
        form = AddAlbumForm()
    else:
        form = AddAlbumForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {
        'form': form,
    }

    return render(request, 'album/add-album.html', context)


def details_album(request, pk):
    album = Album.objects.get(pk=pk)

    context = {
        'album': album
    }

    return render(request, 'album/album-details.html', context)


def edit_album(request, pk):
    album = Album.objects.get(pk=pk)

    if request.method == 'GET':
        form = EditAlbumForm(instance=album)
    else:
        form = EditAlbumForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {
        'album': album,
        'form': form
    }

    return render(request, 'album/edit-album.html', context)


def delete_album(request, pk):
    album = Album.objects.get(pk=pk)

    if request.method == 'GET':
        form = DeleteAlbumForm(instance=album)
    else:
        form = DeleteAlbumForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            # album.delete() -> forms.py
            return redirect('home')

    context = {
        'album': album,
        'form': form
    }

    return render(request, 'album/delete-album.html', context)


def details_profile(request):
    context = {
        'user': get_profile(),
        'albums_len': Album.objects.count()
    }

    return render(request, 'profile/profile-details.html', context)


def delete_profile(request):
        if request.method == 'GET':
            form = ProfileForm()
        else:
            form = ProfileForm(request.POST)
            if form.is_valid():
                form.save()
                albums = Album.objects.all()
                users = Profile.objects.all()
                albums.delete()
                users.delete()
                return redirect('home')

        context = {
            'form': form
        }

        return render(request, 'profile/profile-delete.html', context)
