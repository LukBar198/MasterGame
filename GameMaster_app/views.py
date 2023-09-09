from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from .forms import LoginForm, UserRegistrationForm


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


class DashboardView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'dashboard.html')

# class SessionList(View):
#     def get(self, request):
#         ctx = {
#             'SESSIONS': GameSession
#         }
#         return render(request, 'index.html', ctx)
