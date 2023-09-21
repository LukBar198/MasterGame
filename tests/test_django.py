import pytest
from django.contrib.auth.models import User
from django.contrib.messages import get_messages
from django.urls import reverse

from GameMaster_app.forms import LoginForm, UserRegistrationForm
from GameMaster_app.models import GameMaster, GameSession


@pytest.mark.django_db
def test_get_index_view(client, index_url):
    response = client.get(index_url)
    assert response.status_code == 200
    assert 'login_form' in response.context
    assert isinstance(response.context['login_form'], LoginForm)


@pytest.mark.django_db
def test_valid_login(client, user, index_url, dashboard_url):
    data = {
        'username': 'testuser',
        'password': 'testpassword',
    }
    response = client.post(index_url, data)
    assert response.status_code == 302
    assert response.url == dashboard_url


@pytest.mark.django_db
def test_invalid_login(client, user, index_url):
    data = {
        'username': 'testuser',
        'password': 'wrongpassword',
    }
    response = client.post(index_url, data)
    assert response.status_code == 200
    assert 'Nieprawidlowy login lub hasło' in response.content.decode()


@pytest.mark.django_db
def test_dashboard_view(client, user, index_url, dashboard_url):
    client.login(username='testuser', password='testpassword')
    response = client.get(dashboard_url)
    assert response.status_code in [200, 302]
    if response.status_code == 302:
        assert response.url == index_url


@pytest.mark.django_db
def test_register_view(client, register_url):
    response = client.get(register_url)
    assert response.status_code == 200
    assert 'usr_form' in response.context
    assert isinstance(response.context['usr_form'], UserRegistrationForm)


@pytest.mark.django_db
def test_valid_register(client, register_url):
    data = {
        'username': 'testuser',
        'first_name': 'testuser',
        'email': 'testuser@email.com',
        'password': 'testpassword',
        'password2': 'testpassword',
    }
    response = client.post(register_url, data)
    assert response.status_code in [200, 302]
    assert User.objects.filter(username='testuser').exists()

    if response.status_code == 302:
        assert response.url == reverse('start')


@pytest.mark.django_db
def test_password_mismatch(client, register_url):
    data = {
        'username': 'testuser',
        'first_name': 'testuser',
        'email': 'testuser@email.com',
        'password': 'testpassword',
        'password2': 'wrongpassword',
    }
    response = client.post(register_url, data)
    assert response.status_code == 302
    assert response.url == reverse('register')


@pytest.mark.django_db
def test_user_settings_valid(client, user, settings_url):
    client.login(username='testuser', password='testpassword')
    data = {
        'user_nickname': 'testnickname',
        'is_game_master': True,
    }
    response = client.post(settings_url, data)
    assert response.status_code == 302
    assert response.url == reverse('dashboard')
    assert GameMaster.objects.filter(user_id=user, user_nickname='testnickname', is_game_master=True).exists()


@pytest.mark.django_db
def test_user_settings_invalid(client, user, settings_url):
    client.login(username='testuser', password='testpassword')
    data = {
        'user_nickname': '',
        'is_game_master': True,
    }
    response = client.post(settings_url, data)
    assert response.status_code == 302
    assert response.url == reverse('settings')


@pytest.mark.django_db
def test_add_session_valid(client, gamemaster, add_session_url):
    client.login(username='testuser', password='testpassword')
    data = {
        'title': 'Test Session',
        'slots': 5,
        'date': '2023-09-30',
        'is_open': True,
        'is_public': True,
    }
    response = client.post(add_session_url, data)
    assert response.status_code == 302
    assert response.url == reverse('dashboard')
    assert GameSession.objects.filter(
        title='Test Session',
        slots=5,
        session_date='2023-09-30',
        is_open=True,
        is_public=True
    ).exists()

@pytest.mark.django_db
def test_add_session_view_post_invalid(client, gamemaster, add_session_url):
    client.login(username='testuser', password='testpassword')
    data = {
        'title': '',
        'slots': 5,
        'date': '2023-09-30',
        'is_open': True,
        'is_public': True,
    }
    response = client.post(add_session_url, data)
    assert response.status_code == 302
    assert response.url == reverse('add_session')
