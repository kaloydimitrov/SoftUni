from django import forms


class FirstForm(forms.Form):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    age = forms.IntegerField(min_value=5)
    sex = forms.ChoiceField(
        required=False,
        label='Gender',
        choices=(
            (0, 'None'),
            (1, 'Male'),
            (2, 'Female'),
            (3, "I'd rather not to give")
        ),
    )
