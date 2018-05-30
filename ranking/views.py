from django.shortcuts import render, get_object_or_404, redirect
from .forms import FormRoute, FormAscent, FormDate
from account.models import MyUser
from django.utils import timezone
from dateutil.relativedelta import relativedelta
from .helper_views import ranking_data
from .models import Ascent, Route
from django.contrib.auth.decorators import login_required





def ranking(request):


    seniors_m = []
    seniors_w = []
    juniors_m = []
    juniors_w = []

    time = timezone.now() - relativedelta(years=18)

    if request.method == "POST":
        form = FormDate(request.POST)
        if form.is_valid():
            year = form.cleaned_data['year']
            for user in MyUser.objects.filter(sex='m', date_of_birth__lte=time):
                user_data = ranking_data(user, year)
                seniors_m.append(user_data)

            for user in MyUser.objects.filter(sex='k', date_of_birth__lte=time):
                user_data = ranking_data(user, year)
                seniors_w.append(user_data)

            for user in MyUser.objects.filter(sex='m', date_of_birth__gte=time):
                user_data = ranking_data(user, year)
                juniors_m.append(user_data)

            for user in MyUser.objects.filter(sex='k', date_of_birth__gte=time):
                user_data = ranking_data(user, year)
                juniors_w.append(user_data)

        return render(request, 'ranking/ranking.html',
                      {'form': form, 'seniors_m': seniors_m[:10], 'seniors_w': seniors_w[:10], 'juniors_m': juniors_m[:10],
                       'juniors_w': juniors_w[:10]})
    else:
        form = FormDate()
        year = timezone.now().year
        for user in MyUser.objects.filter(sex='m', date_of_birth__lte=time):
            user_data = ranking_data(user, year)
            seniors_m.append(user_data)

        for user in MyUser.objects.filter(sex='k', date_of_birth__lte=time):
            user_data = ranking_data(user, year)
            seniors_w.append(user_data)

        for user in MyUser.objects.filter(sex='m', date_of_birth__gte=time):
            user_data = ranking_data(user, year)
            juniors_m.append(user_data)

        for user in MyUser.objects.filter(sex='k', date_of_birth__gte=time):
            user_data = ranking_data(user, year)
            juniors_w.append(user_data)


    return render(request, 'ranking/ranking.html', {'form': form, 'seniors_m': seniors_m[:10], 'seniors_w': seniors_w[:10], 'juniors_m': juniors_m[:10],
                                                        'juniors_w': juniors_w[:10]})



def seniors_m(request):
    users = []
    category = "Seniorzy"
    time = timezone.now() - relativedelta(years=18)

    if request.method == "POST":
        form = FormDate(request.POST)
        if form.is_valid():
            year = form.cleaned_data['year']
            for user in MyUser.objects.filter(sex='m', date_of_birth__lte=time):
                user_data = ranking_data(user, year)
                users.append(user_data)

            return render(request, 'ranking/category.html', {'users': users, 'category': category, 'form': form})
    else:
        form = FormDate()
        year = timezone.now().year
        for user in MyUser.objects.filter(sex='m', date_of_birth__lte=time):
            user_data = ranking_data(user, year)
            users.append(user_data)

        return render(request, 'ranking/category.html', {'users': users, 'category': category, 'form': form})

def seniors_w(request):
    users = []
    category = "Seniorki"
    time = timezone.now() - relativedelta(years=18)

    if request.method == "POST":
        form = FormDate(request.POST)
        if form.is_valid():
            year = form.cleaned_data['year']
            for user in MyUser.objects.filter(sex='k', date_of_birth__lte=time):
                user_data = ranking_data(user, year)
                users.append(user_data)
            return render(request, 'ranking/category.html', {'users': users, 'category': category, 'form': form})
    else:
        form = FormDate()
        year = timezone.now().year
        for user in MyUser.objects.filter(sex='k', date_of_birth__lte=time):
            user_data = ranking_data(user, year)
            users.append(user_data)

        return render(request, 'ranking/category.html',
                      {'users': users, 'category': category, 'form': form})

def juniors_m(request):

    users = []
    category = "Juniorzy"
    time = timezone.now() - relativedelta(years=18)
    if request.method == "POST":
        form = FormDate(request.POST)
        if form.is_valid():
            year = form.cleaned_data['year']
            for user in MyUser.objects.filter(sex='m', date_of_birth__gte=time):
                user_data = ranking_data(user, year)
                users.append(user_data)
            return render(request, 'ranking/category.html', {'users': users, 'category': category, 'form': form})

    else:
        form = FormDate()
        year = timezone.now().year
        for user in MyUser.objects.filter(sex='m', date_of_birth__gte=time):
            user_data = ranking_data(user, year)
            users.append(user_data)

        return render(request, 'ranking/category.html',
                      {'users': users, 'category': category, 'form': form})



def juniors_w(request):

    users = []
    category = "Juniorki"
    time = timezone.now() - relativedelta(years=18)
    if request.method == "POST":
        form = FormDate(request.POST)
        if form.is_valid():
            year = form.cleaned_data['year']
            for user in MyUser.objects.filter(sex='k', date_of_birth__gte=time):
                user_data = ranking_data(user, year)
                users.append(user_data)
            return render(request, 'ranking/category.html', {'users': users, 'category': category, 'form': form})
    else:
        form = FormDate()
        year = timezone.now().year
        for user in MyUser.objects.filter(sex='k', date_of_birth__gte=time):
            user_data = ranking_data(user, year)
            users.append(user_data)

        return render(request, 'ranking/category.html',
                      {'users': users, 'category': category, 'form': form})


def ascents(request, pk):
    ascents = get_object_or_404(MyUser, pk=pk)

    return render(request, 'ranking/ascents.html', {'ascents': ascents})



def ascents_logged_user(request):

    ascents = get_object_or_404(MyUser, pk=request.user.id)
    return render(request, 'ranking/ascents_logged_user.html', {'ascents': ascents})


@login_required
def new_ascent(request):
    if request.method == 'POST':
        form1 = FormRoute(request.POST)
        form2 = FormAscent(request.POST)

        if form1.is_valid() and form2.is_valid():
            cd1 = form1.cleaned_data
            cd2 = form2.cleaned_data
            new_route = form1.save(commit=False)
            new_ascent = form2.save(commit=False)
            check = Route.objects.filter(name=cd1['name'].lower().capitalize(), crag=cd1['crag'].lower().capitalize(),
                                               grade=cd1['grade'].lower())
            if check.count() > 0:
                given_route = Route.objects.get(name=cd1['name'].lower().capitalize(),
                                                 crag=cd1['crag'].lower().capitalize(), grade=cd1['grade'].lower())
                new_ascent.style = cd2['style'].lower()
                new_ascent.date_of_birth = cd2['date_of_birth']

                if cd2['style'] == 'rp':
                    for i in Ascent.rp:
                        if given_route.grade == i:
                            new_ascent.points = Ascent.rp[i]

                elif cd2['style'] == "os":
                    for i in Ascent.os:
                        if given_route.grade == i:
                            new_ascent.points = Ascent.os[i]

                elif cd2['style'] == "fl":
                    for i in Ascent.fl:
                        if given_route.grade == i:
                            new_ascent.points = Ascent.fl[i]

                new_ascent.user = request.user
                new_ascent.route = given_route
                new_ascent.save()
                return redirect("ranking")

            else:
                if cd2['style'] == 'rp':
                    for i in Ascent.rp:
                        if cd1['grade'] == i:
                            new_ascent.points = Ascent.rp[i]

                elif cd2['style'] == "os":
                    for i in Ascent.os:
                        if cd1['grade'] == i:
                            new_ascent.points = Ascent.os[i]

                elif cd2['style'] == "fl":
                    for i in Ascent.fl:
                        if cd1['grade'] == i:
                            new_ascent.points = Ascent.fl[i]

                new_route.save()
                new_ascent.user = request.user
                new_ascent.route = new_route
                new_ascent.save()
                return redirect("ranking")
    else:
        form1 = FormRoute(request.POST)
        form2 = FormAscent(request.POST)
    return render(request, 'ranking/new_ascent.html', {'form1': form1, 'form2': form2})

@login_required
def ascent_edit(request, pk):
    ascent = get_object_or_404(Ascent, pk=pk)
    route = ascent.route

    if request.method == 'POST':
        form1 = FormRoute(instance=route, data=request.POST)
        form2 = FormAscent(instance=ascent, data=request.POST)

        if form1.is_valid() and form2.is_valid():
            form1.save()
            form2.save()
            return render(request, 'ranking/edit_complete.html', {'form1': form1, 'form2': form2})
    else:
        form1 = FormRoute(instance=route)
        form2 = FormAscent(instance=ascent)

    return render(request, 'ranking/ascent_edit.html', {'form1': form1, 'form2': form2})