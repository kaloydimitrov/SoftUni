from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Profile


def get_profile():
    # try:
    #     Profile.objects.get()
    # except:
    #     return None
    return True


def index(request):
    profile = get_profile

    if profile is None:
        return render(request, 'core/home-no-profile.html')

    return render(request, 'core/home-with-profile.html')


def add_album(request):
    return render(request, 'album/add-album.html')


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
