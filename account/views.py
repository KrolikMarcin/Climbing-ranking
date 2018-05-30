from django.shortcuts import render
from .forms import UserRegistration, UserEditForm
from django.contrib.auth.decorators import login_required


@login_required
def dashboard(request):
    return render(request, 'account/dashboard.html', {'section': 'dashboard'})

def register(request):
    if request.method == 'POST':
        user_form = UserRegistration(request.POST)
        if user_form.is_valid():

            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password1'])
            new_user.save()
            return render(request, 'account/register_done.html', {'new_user': new_user})
        else:
            return render(request, 'account/register_fail.html', {})
    else:
        user_form = UserRegistration()
        return render(request, 'account/register.html', {'user_form': user_form})

@login_required
def edit(request):

    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user, data=request.POST)
        if user_form.is_valid():
            user_form.save()
            user = request.user
            return render(request, 'account/edit_complete.html', {'user': user})
    else:
        user_form = UserEditForm(instance=request.user)

    return render(request, 'account/edit.html', {'user_form': user_form})



# def register(request):      Ostatni widok
#     if request.method == 'POST':
#         user_form = UserRegistration(request.POST)
#         if user_form.is_valid():
#             new_user = Uzytkownik()
#             cd = user_form.cleaned_data
#             new_user.nazwa_uzytkownika = cd['nazwa_uzytkownika']
#             new_user.imie = cd['imie']
#             new_user.nazwisko = cd['nazwisko']
#             new_user.data_urodzenia= cd['data_urodzenia']
#             new_user.plec = cd['plec']
#             new_user.set_password(cd['password'])
#             new_user.save()
#
#
#
#
#             return render(request, 'account/register_done.html', {'new_user': new_user})
#
#     else:
#         user_form = UserRegistration()
#         return render(request, 'account/register.html', {'user_form': user_form})





# def user_login(request):
#     if request.method == "POST":
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             cd = form.cleaned_data
#             user = authenticate(username=cd['username'], password=cd['password'])
#             if user is not None:
#                 if user.is_active:
#                     login(request, user)
#                     return HttpResponse('Uwierzytelnie zakonczone sukcesem')
#                 else:
#                     HttpResponse('Konto jest zablokowane')
#             else:
#                 HttpResponse('Nieprawidlowe dane')
#
#     else:
#         form = LoginForm()
#     return  render(request, 'registration/login.html', {'form': form})