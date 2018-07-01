from django import forms
from django.utils import timezone


class FormDate(forms.Form):
    year_choices = []
    for i in range(1990, timezone.now().year+1):
        year_choices.append((i, i))
    years = reversed(tuple(year_choices))
    year = forms.ChoiceField(widget=forms.Select, choices=years)