from django.contrib.auth.models import User
from django.urls import reverse
from django.test import Client
import pytest

from GameMaster_app.models import GameMaster


@pytest.fixture
def client():
    return Client()


@pytest.fixture
def user():
    return User.objects.create_user(username='testuser', password='testpassword')


@pytest.fixture
def gamemaster():
    user = User.objects.create_user(username='testuser', password='testpassword')
    GameMaster.objects.create(user_id=user, user_nickname='testnickname', is_game_master=True)
    return user


@pytest.fixture
def dashboard_url():
    return reverse('dashboard')


@pytest.fixture
def index_url():
    return reverse('index')


@pytest.fixture
def register_url():
    return reverse('register')


@pytest.fixture
def settings_url():
    return reverse('settings')


@pytest.fixture
def add_session_url():
    return reverse('add_session')
