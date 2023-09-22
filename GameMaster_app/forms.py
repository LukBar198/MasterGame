from django import forms
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    """
    LoginForm is a Django form used for user login.

    This form includes fields for the username and password.

    Fields:
    - username (CharField): A character field for entering the username.
    - password (CharField with PasswordInput widget): A character field for entering the password
      with a password input widget for secure input.
    """

    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class UserRegistrationForm(forms.ModelForm):
    """
    UserRegistrationForm is a Django ModelForm for user registration.

    This form allows users to register by providing a username, first name, and email. It also
    includes fields for password and password confirmation.

    Fields:
    - username (CharField): A character field for entering the username.
    - first_name (CharField): A character field for entering the user's first name.
    - email (CharField): A character field for entering the user's email address.
    - password (CharField with PasswordInput widget): A character field for entering the password
      with a password input widget for secure input.
    - password2 (CharField with PasswordInput widget): A character field for repeating the password,
      also with a password input widget.

    Meta:
    - model (User): Specifies the User model as the source of data for this form.
    - fields (list): Specifies the fields to include in the form, including 'username', 'first_name',
      and 'email'.

    Methods:
    - clean_password2(): A custom validation method to ensure that the 'password' and 'password2' fields
      have matching values.
    """

    password = forms.CharField(label='Password',
                               widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password',
                                widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'email']

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Hasła nie są identyczne')
        return cd['password2']
