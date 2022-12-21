from django.shortcuts import render, redirect
from .models import Profile, Plant
from .forms import ProfileForm, DeleteProfileForm, EditProfileForm, PlantForm, DeletePlantForm


def get_profile():
    try:
        return Profile.objects.get()
    except Profile.DoesNotExist:
        return None


def index(request):
    profile = get_profile()
    do_not_show = False

    if profile is None:
        do_not_show = True

    context = {
        'nav_bar': do_not_show
    }

    return render(request, 'home-page.html', context)


def create_profile(request):
    if request.method == 'GET':
        form = ProfileForm()
    else:
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogue')

    context = {
        'form': form,
        'nav_bar': True
    }

    return render(request, 'create-profile.html', context)


def catalogue(request):
    plants = Plant.objects.all()
    context = {
        'plants': plants
    }

    return render(request, 'catalogue.html', context)


def create_plant(request):
    if request.method == 'GET':
        form = PlantForm()
    else:
        form = PlantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogue')

    context = {
        'form': form,
    }

    return render(request, 'create-plant.html', context)


def plant_details(request, pk):
    plant = Plant.objects.get(pk=pk)

    context = {
        'plant': plant
    }

    return render(request, 'plant-details.html', context)


def edit_plant(request, pk):
    plant = Plant.objects.get(pk=pk)
    if request.method == 'GET':
        form = PlantForm(instance=plant)
    else:
        form = PlantForm(request.POST, instance=plant)
        if form.is_valid():
            form.save()
            return redirect('catalogue')

    context = {
        'form': form,
        'plant': plant
    }

    return render(request, 'edit-plant.html', context)


def delete_plant(request, pk):
    plant = Plant.objects.get(pk=pk)
    if request.method == 'GET':
        form = DeletePlantForm(instance=plant)
    else:
        form = DeletePlantForm(request.POST, instance=plant)
        if form.is_valid():
            form.save()
            return redirect('catalogue')

    context = {
        'form': form,
        'plant': plant
    }

    return render(request, 'delete-plant.html', context)


def profile_details(request):
    user = get_profile()
    plants = Plant.objects.count()

    context = {
        'user': user,
        'plants_count': plants
    }

    return render(request, 'profile-details.html', context)


def edit_profile(request):
    profile = get_profile()

    if request.method == 'GET':
        form = EditProfileForm(instance=profile)
    else:
        form = EditProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile details')

    context = {
        'form': form,
    }

    return render(request, 'edit-profile.html', context)


def delete_profile(request):
    if request.method == 'GET':
        form = DeleteProfileForm()
    else:
        form = DeleteProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {
        'form': form,
    }

    return render(request, 'delete-profile.html', context)
