from django import forms
from .models import Profile, Plant


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['username', 'first_name', 'last_name']
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name'
        }


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'profile_picture': 'Profile Picture',
        }


class DeleteProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ()

    def save(self, commit=True):
        Profile.objects.all().delete()
        Plant.objects.all().delete()


class PlantForm(forms.ModelForm):
    class Meta:
        model = Plant
        fields = '__all__'
        labels = {
            'plant_type': 'Type',
            'image_url': 'Image URL'
        }


class DeletePlantForm(forms.ModelForm):
    class Meta:
        model = Plant
        fields = '__all__'
        labels = {
            'plant_type': 'Type',
            'image_url': 'Image URL'
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs['readonly'] = 'readonly'
            self.fields['plant_type'].disabled = True

    def save(self, commit=True):
        self.instance.delete()
        return self.instance
