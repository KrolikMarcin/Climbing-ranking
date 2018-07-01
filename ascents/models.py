from django.db import models
from django.conf import settings


class Route(models.Model):
    grades = (('6a', '6a'), ('6a+', '6a+'), ('6b', '6b'), ('6b+', '6b+'), ('6c', '6c'), ('6c+', '6c+'), ('7a', '7a'),
              ('7a+', '7a+'), ('7b', '7b'), ('7b+', '7b+'), ('7c', '7c'), ('7c+', '7c+'), ('8a', '8a'), ('8a+', '8a+'),
              ('8b', '8b'), ('8b+', '8b+'), ('8c', '8c'), ('8c+', '8c+'), ('9a', '9a'), ('9a+', '9a+'), ('9b', '9b'),
              ('9b+', '9b+'))

    name = models.CharField(max_length=50)
    crag = models.CharField(max_length=30)
    sector = models.CharField(max_length=30, blank=True)
    grade = models.CharField(max_length=3, choices=grades)
    user = models.ManyToManyField(settings.AUTH_USER_MODEL, through='Ascent')

    def __str__(self):
        return "{name} {crag} {grade}".format(name=self.name, crag=self.crag, grade=self.grade)


class Ascent(models.Model):


    styles = (
        ('fl', 'fl'),
        ('rp', 'rp'),
        ('os', 'os'),
    )

    date_ascent = models.DateField()
    style = models.CharField(max_length=2, choices=styles)
    points = models.IntegerField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_ascents')
    route = models.ForeignKey(Route, on_delete=models.CASCADE)

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
            if str(grade) == i:
                return style[i]

    class Meta:
        ordering = ['-points', '-date_ascent']

    rp = {"6a": 100, "6a+": 150, "6b": 200, "6b+": 250, "6c": 300, "6c+": 350, "7a": 400, "7a+": 450, "7b": 500,
          "7b+": 550, "7c": 600, "7c+": 650, "8a": 700, "8a+": 750, "8b": 800, "8b+": 850, "8c": 900, "8c+": 950,
          "9a": 1000, "9a+": 1050, "9b": 1100, "9b+": 1150}

    fl = {"6a": 150, "6a+": 200, "6b": 250, "6b+": 300, "6c": 350, "6c+": 400, "7a": 450, "7a+": 500, "7b": 550,
          "7b+": 600, "7c": 650, "7c+": 700, "8a": 750, "8a+": 800, "8b": 850, "8b+": 900, "8c": 950, "8c+": 1000,
          "9a": 1050, "9a+": 1100, "9b": 1150, "9b+": 1200}

    os = {"6a": 225, "6a+": 275, "6b": 325, "6b+": 375, "6c": 425, "6c+": 475, "7a": 525, "7a+": 575, "7b": 625,
          "7b+": 675, "7c": 725, "7c+": 775, "8a": 825, "8a+": 875, "8b": 925, "8b+": 975, "8c": 1025, "8c+": 1075,
          "9a": 1125, "9a+": 1175, "9b": 1225, "9b+": 1275}

    def __str__(self):
        return "{user} {route} {date_ascent} {style} {points}".format(
            user=self.user, route=self.route, date_ascent=self.date_ascent, style=self.style, points=self.points)