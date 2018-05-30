from django import forms
from .models import Route, Ascent
from django.utils import timezone


class FormRoute(forms.ModelForm):
    class Meta:
        model = Route
        fields = ['name', 'crag', 'sector', 'grade']
        labels = {'name': 'Nazwa', 'crag': 'Rejon', 'sector': 'Sector', 'grade': 'Wycena'}

class FormAscent(forms.ModelForm):
    class Meta:
        model = Ascent
        fields = ['date_ascent', 'style']
        labels= {'date_ascent': 'Data przejścia', 'style': 'Styl'}

class FormDate(forms.Form):
    year_choices = []
    for i in range(1990, timezone.now().year+1):
        year_choices.append((i, i))
    years = reversed(tuple(year_choices))
    year = forms.ChoiceField(widget=forms.Select, choices=years)