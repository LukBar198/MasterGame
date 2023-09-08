from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.contrib import messages
from .forms import LoginForm


class IndexView(View):
    def get(self, request):
        login_form = AuthenticationForm()
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
                    return HttpResponse('Logowanie OK')
                else:
                    return HttpResponse('Konto zablokowane')
            else:
                messages.error(request, 'Nieprawidłowy login lub hasło.')
        else:
            login_form = LoginForm()
        return render(request, 'index.html', {'login_form': login_form})

# class SessionList(View):
#     def get(self, request):
#         ctx = {
#             'SESSIONS': GameSession
#         }
#         return render(request, 'index.html', ctx)
