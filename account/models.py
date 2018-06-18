from django.db import models
from django.db.models import Sum
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

class MyUser(AbstractUser):

    date_of_birth = models.DateField(blank=True, null=True)
    sex = models.CharField(max_length=1, blank=True, null=True)


    def get_ascents(self, year):
        ascents = self.user_ascents.filter(date_ascent__year=year)
        return ascents

    def get_sum_points(self, year=timezone.now().year):
        sum_points = self.user_ascents.all().filter(date_ascent__year=year).order_by('-points')[:10].aggregate(Sum('points'))['points__sum']
        if sum_points != None:

            return sum_points

    def ranking_data(self, year):
        if self.get_sum_points(year):
            ranking_data = {}

            ranking_data.update({'pk': self.pk})
            ranking_data.update({'date_of_birth': self.date_of_birth})
            ranking_data.update({'first_name': self.first_name})
            ranking_data.update({'last_name': self.last_name})
            ranking_data.update({'sum_points': self.get_sum_points(year)})
            return ranking_data
