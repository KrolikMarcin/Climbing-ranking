
from django.db.models import Sum
from dateutil.relativedelta import relativedelta
from django.utils import timezone



def ranking_data(user, year):

    user_data = []
    user_data.append(user.pk)
    user_data.append({'date_of_birth': user.date_of_birth})
    user_data.append({'first_name': user.first_name})
    user_data.append({'last_name': user.last_name})
    if user.ascent_set.all().filter(date_ascent__year=year).order_by('-points')[:10].aggregate(Sum('points'))['points__sum'] == None:
        user_data.append({'points': 0})
    else:
        user_data.append({'points': user.ascent_set.all().filter(date_ascent__year=year).order_by('-points')[:10].aggregate(Sum('points'))['points__sum']})
    return user_data


