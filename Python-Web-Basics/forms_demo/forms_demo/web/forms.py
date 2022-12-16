from django import forms


class FirstForm(forms.Form):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    age = forms.IntegerField(min_value=5, initial=0)
    sex = forms.ChoiceField(
        required=False,
        label='Gender',
        choices=(
            (0, 'None'),
            (1, 'Male'),
            (2, 'Female'),
            (3, "I'd rather not to give"),
        ))
    address = forms.CharField(max_length=300, widget=forms.Textarea(
        attrs={
            'cols': 20, 'rows': 5,
            'class': 'special',
            'title': 'add comment'
        }))
    radio_buttons = forms.ChoiceField(
        choices=(
            (0, 'None'),
            (1, 'One'),
            (2, 'Two'),
            (3, 'Three'),
        ))
