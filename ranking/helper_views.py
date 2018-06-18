from django.utils import timezone
from operator import itemgetter


def category_data(category, year=timezone.now().year):
    category_users = []

    for user in category:

        if user.ranking_data(year) != None:
            category_users.append(user.ranking_data(year))

    category_users = sorted(category_users, key=itemgetter('sum_points'), reverse=True)

    return category_users