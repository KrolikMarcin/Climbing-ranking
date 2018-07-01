from django import forms
from .models import Route, Ascent


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

    def check_style(self, style):
        if style == 'rp':
            return self.rp
        elif style == 'fl':
            return self.fl
        elif style == 'os':
            return self.os

    def points_converter(self, style, grade):

        style = self.check_style(style)
        for i in style:
            if grade == i:
                return style[i]

