from django.shortcuts import render, get_object_or_404, redirect
from .forms import FormRoute, FormAscent
from ranking.forms import FormDate
from account.models import MyUser
from django.utils import timezone
from .models import Ascent, Route
from django.contrib.auth.decorators import login_required
# Create your views here.

def ascents(request, pk):
    user = get_object_or_404(MyUser, pk=pk)
    if request.method == 'POST':
        form = FormDate(request.POST)
        if form.is_valid():
            year = form.cleaned_data['year']
            ascents = user.get_ascents(year)
            sum_points = user.get_sum_points(year)
            return render(request, 'ascents/ascents.html', {'ascents': ascents, 'form': form, 'sum_points': sum_points})

    else:

        form =FormDate()
        year = timezone.now().year
        ascents = user.get_ascents(year)
        sum_points = user.get_sum_points()
        return render(request, 'ascents/ascents.html', {'ascents': ascents, 'form': form, 'user': user, 'sum_points': sum_points})


@login_required
def new_ascent(request):
    if request.method == 'POST':

        form_route = FormRoute(request.POST)
        form_ascent = FormAscent(request.POST)

        if form_route.is_valid() and form_ascent.is_valid():

            cd_route = form_route.cleaned_data
            cd_ascent = form_ascent.cleaned_data
            new_route = form_route.save(commit=False)
            new_ascent = form_ascent.save(commit=False)
            check = Route.objects.filter(name=cd_route['name'].lower().capitalize(), crag=cd_route['crag'].lower().capitalize(),
                                               grade=cd_route['grade'])

            if check.count() > 0:

                given_route = Route.objects.get(name=cd_route['name'].lower().capitalize(), crag=cd_route['crag'].lower().capitalize(),
                                               grade=cd_route['grade'])

                new_ascent.points = new_ascent.points_converter(style=cd_ascent['style'], grade=cd_route['grade'])
                new_ascent.user = request.user
                new_ascent.route = given_route
                new_ascent.save()


            else:

                new_ascent.points = new_ascent.points_converter(style=cd_ascent['style'], grade=cd_route['grade'])
                new_route.save()
                new_ascent.user = request.user
                new_ascent.route = new_route
                new_ascent.save()

            return redirect('ranking')

    else:
        form_route = FormRoute(request.POST)
        form_ascent = FormAscent(request.POST)

    return render(request, 'ascents/new_ascent.html', {'form_route': form_route, 'form_ascent': form_ascent})

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

            return render(request, 'ascents/edit_complete.html', {'form1': form1, 'form2': form2, 'pk': pk})
    else:
        form1 = FormRoute(instance=route)
        form2 = FormAscent(instance=ascent)

    return render(request, 'ascents/ascent_edit.html', {'form1': form1, 'form2': form2})