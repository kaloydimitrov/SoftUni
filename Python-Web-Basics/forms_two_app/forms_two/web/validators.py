from django.core.exceptions import ValidationError


def is_upper(value):
    if not value[0].isupper():
        raise ValidationError('First letter should be upper')


def less_than_10(value):
    if value < 10:
        raise ValidationError('Age cannot be less than 10')


def more_than_65(value):
    if value > 65:
        raise ValidationError('Age cannot be higher than 65')
