from django.shortcuts import render, get_object_or_404, redirect
from .forms import FormDate
from account.models import MyUser
from django.utils import timezone
from dateutil.relativedelta import relativedelta
from .helper_views import category_data


def ranking(request):

    time = timezone.now() - relativedelta(years=18)
    seniors_m = MyUser.objects.filter(sex='m', date_of_birth__lte=time)
    seniors_w = MyUser.objects.filter(sex='w', date_of_birth__lte=time)
    juniors_m = MyUser.objects.filter(sex='m', date_of_birth__gte=time)
    juniors_w = MyUser.objects.filter(sex='w', date_of_birth__gte=time)

    if request.method == "POST":
        form = FormDate(request.POST)
        if form.is_valid():
            year = form.cleaned_data['year']
            seniors_m = category_data(seniors_m, year)
            seniors_w = category_data(seniors_w, year)
            juniors_m = category_data(juniors_m, year)
            juniors_w = category_data(juniors_w, year)

        return render(request, 'ranking/ranking.html',
                      {'form': form, 'seniors_m': seniors_m[:10], 'seniors_w': seniors_w[:10], 'juniors_m': juniors_m[:10],
                       'juniors_w': juniors_w[:10]})
    else:
        form = FormDate()

        seniors_m = category_data(seniors_m)
        seniors_w = category_data(seniors_w)
        juniors_m = category_data(juniors_m)
        juniors_w = category_data(juniors_w)

        return render(request, 'ranking/ranking.html', {'form': form, 'seniors_m': seniors_m[:10], 'seniors_w': seniors_w[:10], 'juniors_m': juniors_m[:10],
                                                        'juniors_w': juniors_w[:10]})


def category(request, category):
    time = timezone.now() - relativedelta(years=18)

    if category == 'seniors_m':
        category_name = 'Seniorzy'
        players = MyUser.objects.filter(sex='m', date_of_birth__lte=time)
    elif category == 'seniors_w':
        category_name = 'Seniorki'
        players = MyUser.objects.filter(sex='w', date_of_birth__lte=time)
    elif category == 'juniors_m':
        category_name = 'Juniorzy'
        players = MyUser.objects.filter(sex='m', date_of_birth__gte=time)
    elif category == 'juniors_w':
        category_name = 'Juniorki'
        players = MyUser.objects.filter(sex='w', date_of_birth__gte=time)


    if request.method == "POST":
        form = FormDate(request.POST)
        if form.is_valid():
            year = form.cleaned_data['year']
            users = category_data(players, year)

            return render(request, 'ranking/category.html', {'users': users, 'category_name': category_name, 'form': form})

    else:
        form = FormDate()
        users = category_data(players)

        return render(request, 'ranking/category.html', {'users': users, 'category_name': category_name, 'form': form})