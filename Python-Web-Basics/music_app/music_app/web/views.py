from django.http import HttpResponse
from django.shortcuts import render


def add_album(request):
    return render(request, 'add-album.html')


def details_album(request):
    return render(request, 'album-details.html')


def edit_album(request):
    return render(request, 'edit-album.html')


def delete_album(request):
    return render(request, 'delete-album.html')


def details_profile(request):
    return render(request, 'profile-details.html')


def delete_profile(request):
    return render(request, 'profile-delete.html')
