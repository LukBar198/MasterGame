import pytest
from django.contrib.auth.models import User
from django.contrib.messages import get_messages
from django.urls import reverse

from GameMaster_app.forms import LoginForm, UserRegistrationForm
from GameMaster_app.models import GameMaster, GameSession


@pytest.mark.django_db
def test_get_index_view(client, index_url):
    """
    Test the GET request to the index view.

    Args:
    - client (django.test.Client): The Django test client.
    - index_url (str): The URL for the index view.

    This test checks that the index view returns a status code of 200 (OK),
    that it includes a 'login_form' in the context, and that the form
    in the context is an instance of the LoginForm class.
    """
    response = client.get(index_url)
    assert response.status_code == 200
    assert 'login_form' in response.context
    assert isinstance(response.context['login_form'], LoginForm)


@pytest.mark.django_db
def test_valid_login(client, user, index_url, dashboard_url):
    """
    Test a valid user login.

    Args:
    - client (django.test.Client): The Django test client.
    - user (User): An instance of the User model for testing.
    - index_url (str): The URL for the index view.
    - dashboard_url (str): The URL for the dashboard view.

    This test checks that a valid user can log in successfully. It sends a
    POST request with valid user credentials to the index view and checks
    that the response redirects to the dashboard.
    """
    data = {
        'username': 'testuser',
        'password': 'testpassword',
    }
    response = client.post(index_url, data)
    assert response.status_code == 302
    assert response.url == dashboard_url


@pytest.mark.django_db
def test_invalid_login(client, user, index_url):
    """
    Test an invalid user login.

    Args:
    - client (django.test.Client): The Django test client.
    - user (User): An instance of the User model for testing.
    - index_url (str): The URL for the index view.

    This test checks that an invalid login attempt results in a status code of 200 (OK)
    and that the response content contains the message 'Nieprawidlowy login lub hasło'.
    """
    data = {
        'username': 'testuser',
        'password': 'wrongpassword',
    }
    response = client.post(index_url, data)
    assert response.status_code == 200
    assert 'Nieprawidlowy login lub hasło' in response.content.decode()


@pytest.mark.django_db
def test_dashboard_view(client, user, index_url, dashboard_url):
    """
    Test access to the dashboard view.

    Args:
    - client (django.test.Client): The Django test client.
    - user (User): An instance of the User model for testing.
    - index_url (str): The URL for the index view.
    - dashboard_url (str): The URL for the dashboard view.

    This test checks that an authenticated user can access the dashboard view.
    It logs in a user, sends a GET request to the dashboard view, and checks
    that the response status code is either 200 (OK) or 302 (redirect to the index).
    """
    client.login(username='testuser', password='testpassword')
    response = client.get(dashboard_url)
    assert response.status_code in [200, 302]
    if response.status_code == 302:
        assert response.url == index_url


@pytest.mark.django_db
def test_register_view(client, register_url):
    """
    Test the registration view.

    Args:
    - client (django.test.Client): The Django test client.
    - register_url (str): The URL for the registration view.

    This test checks that the registration view returns a status code of 200 (OK),
    that it includes a 'usr_form' in the context, and that the form
    in the context is an instance of the UserRegistrationForm class.
    """
    response = client.get(register_url)
    assert response.status_code == 200
    assert 'usr_form' in response.context
    assert isinstance(response.context['usr_form'], UserRegistrationForm)


@pytest.mark.django_db
def test_valid_register(client, register_url):
    """
    Test a valid user registration.

    Args:
    - client (django.test.Client): The Django test client.
    - register_url (str): The URL for the registration view.

    This test checks that a user can register successfully. It sends a
    POST request with valid user registration data to the registration view
    and checks that the response status code is either 200 (OK) or 302
    (redirect to 'start'). It also checks if the User model records the new user.
    """
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
    """
    Test user registration with mismatched passwords.

    Args:
    - client (django.test.Client): The Django test client.
    - register_url (str): The URL for the registration view.

    This test checks that when a user submits a registration form with mismatched
    passwords, it displays an error message. It sends a POST request with mismatched
    passwords, follows the redirect, and checks that the response status code is 200 (OK),
    and the error message is displayed on the page.
    """
    data = {
        'username': 'testuser',
        'first_name': 'testuser',
        'email': 'testuser@email.com',
        'password': 'testpassword',
        'password2': 'wrongpassword',
    }
    response = client.post(register_url, data, follow=True)
    messages = list(get_messages(response.wsgi_request))
    message = messages[0]
    assert response.status_code == 200
    assert messages
    assert "Hasła nie są takie same!" in message.message
    assert response.request['PATH_INFO'] == reverse('register')


@pytest.mark.django_db
def test_user_settings_valid(client, user, settings_url):
    """
    Test user settings update with valid data.

    Args:
    - client (django.test.Client): The Django test client.
    - user (User): An instance of the User model for testing.
    - settings_url (str): The URL for the user settings view.

    This test checks that a user can update their settings with valid data.
    It logs in a user, sends a POST request with valid settings data to the
    user settings view, and checks that the response redirects to the dashboard.
    It also checks if the GameMaster model records the user role change.
    """
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
    """
    Test user settings update with invalid data.

    Args:
    - client (django.test.Client): The Django test client.
    - user (User): An instance of the User model for testing.
    - settings_url (str): The URL for the user settings view.

    This test checks that when a user submits invalid settings data, it displays
    an error message. It logs in a user, sends a POST request with invalid settings
    data, follows the redirect, and checks that the response status code is 200 (OK),
    and the error message is displayed on the page.
    """
    client.login(username='testuser', password='testpassword')
    data = {
        'user_nickname': '',
        'is_game_master': True,
    }
    response = client.post(settings_url, data, follow=True)
    messages = list(get_messages(response.wsgi_request))
    message = messages[0]
    assert response.status_code == 200
    assert messages
    assert "Wypełnij poprawnie wszystkie pola" in message.message
    assert response.request['PATH_INFO'] == reverse('settings')


@pytest.mark.django_db
def test_add_session_valid(client, gamemaster, add_session_url):
    """
    Test adding a valid game session.

    Args:
    - client (django.test.Client): The Django test client.
    - gamemaster (GameMaster): An instance of the GameMaster model for testing.
    - add_session_url (str): The URL for adding a game session.

    This test checks that a user with game master privileges can add a valid
    game session. It logs in a user with game master privileges, sends a POST
    request with valid game session data to the add session view, and checks
    that the response redirects to the dashboard. It also checks if the
    GameSession model records the new session.
    """
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
def test_add_session_invalid(client, gamemaster, add_session_url):
    """
    Test adding an invalid game session.

    Args:
    - client (django.test.Client): The Django test client.
    - gamemaster (GameMaster): An instance of the GameMaster model for testing.
    - add_session_url (str): The URL for adding a game session.

    This test checks that when a user with game master privileges submits an
    invalid game session, it displays an error message. It logs in a user with
    game master privileges, sends a POST request with invalid game session data,
    follows the redirect, and checks that the response status code is 200 (OK),
    and the error message is displayed on the page.
    """
    client.login(username='testuser', password='testpassword')
    data = {
        'title': '',
        'slots': 5,
        'date': '2023-09-30',
        'is_open': True,
        'is_public': True,
    }
    response = client.post(add_session_url, data, follow=True)
    messages = list(get_messages(response.wsgi_request))
    message = messages[0]
    assert response.status_code == 200
    assert messages
    assert "Wypełnij poprawnie wszystkie pola" in message.message
    assert response.request['PATH_INFO'] == reverse('add_session')



