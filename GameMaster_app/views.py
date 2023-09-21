from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from .forms import LoginForm, UserRegistrationForm
from .models import GameSession, GameMaster


class IndexView(View):
    def get(self, request):
        login_form = LoginForm()
        return render(request, 'index.html', {'login_form': login_form})

    def post(self, request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            cd = login_form.cleaned_data
            user = authenticate(request,
                                username=cd['username'],
                                password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    messages.success(request, 'Logowanie zakończone pomyślnie')
                    return redirect('dashboard')
                else:
                    return HttpResponse('Konto zablokowane')
            else:
                return HttpResponse('Nieprawidlowy login lub hasło')
        else:
            login_form = LoginForm()
        return render(request, 'index.html', {'login_form': login_form})


class RegisterView(View):
    def get(self, request):
        usr_form = UserRegistrationForm()
        return render(request, 'register.html', {'usr_form': usr_form})

    def post(self, request):
        usr_form = UserRegistrationForm(request.POST)
        if usr_form.is_valid():
            new_user = usr_form.save(commit=False)
            new_user.set_password(usr_form.cleaned_data['password'])
            new_user.save()
            return render(request, 'start.html', {'new_user': new_user})
        messages.error(request, f"Hasła nie są takie same!")
        return redirect('register')


class DashboardView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'dashboard.html')


class UserSettingsView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'settings.html')

    def post(self, request):
        user_id = request.user.id
        user = User.objects.get(id=user_id)
        user_nickname = request.POST.get('user_nickname')
        is_game_master = request.POST.get('is_game_master')
        if user_nickname and is_game_master:
            GameMaster.objects.create(
                user_id=user,
                user_nickname=user_nickname,
                is_game_master=True
            )
            return redirect('dashboard')
        messages.error(request, f"Wypełnij poprawnie wszystkie pola")
        return redirect('settings')


class AddSessionView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'add_session.html')

    def post(self, request):
        owner_id = request.user.id
        owner = GameMaster.objects.get(user_id=owner_id)
        title = request.POST.get('title')
        slots = request.POST.get('slots')
        date = request.POST.get('date')
        is_open = request.POST.get('is_open')
        is_public = request.POST.get('is_public')
        if title and slots and date and is_open and is_public:
            GameSession.objects.create(
                owner_id=owner,
                title=title,
                slots=int(slots),
                session_date=date,
                is_open=True,
                is_public=True
            )
            return redirect('dashboard')
        messages.error(request, f"Wypełnij poprawnie wszystkie pola")
        return redirect('add_session')

