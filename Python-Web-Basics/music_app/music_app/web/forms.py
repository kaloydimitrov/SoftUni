from django import forms
from .models import Profile, Album


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


class BaseAlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = '__all__'
        widgets = {
            'album_name': forms.TextInput(
                attrs={
                    'placeholder': 'Album Name',
                }
            ),
            'artist': forms.TextInput(
                attrs={
                    'placeholder': 'Artist',
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'placeholder': 'Description',
                }
            ),
            'image_url': forms.URLInput(
                attrs={
                    'placeholder': 'Image URL',
                }
            ),
            'price': forms.NumberInput(
                attrs={
                    'placeholder': 'Price',
                }
            ),
        }


class AddAlbumForm(BaseAlbumForm):
    pass


class EditAlbumForm(BaseAlbumForm):
    pass


class DeleteAlbumForm(BaseAlbumForm):
    def save(self, commit=True):
        if commit:
            self.instance.delete()

        return self.instance
