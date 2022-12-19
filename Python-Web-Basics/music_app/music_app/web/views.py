from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Profile, Album
from .forms import ProfileForm, AlbumForm


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
        form = AlbumForm()
    else:
        form = AlbumForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {
        'form': form,
    }

    return render(request, 'album/add-album.html', context)


def details_album(request, pk):
    return render(request, 'album/album-details.html')


def edit_album(request, pk):
    return render(request, 'album/edit-album.html')


def delete_album(request, pk):
    return render(request, 'album/delete-album.html')


def details_profile(request):
    return render(request, 'profile/profile-details.html')


def delete_profile(request):
    return render(request, 'profile/profile-delete.html')
