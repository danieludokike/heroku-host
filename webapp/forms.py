from django import forms


# Forms to be inherited from
class BaseForm(forms.Form):
    """The registration and the login form inherits from this"""
    username = forms.CharField(
        max_length=200,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            }
        )
    )
    password = forms.CharField(
        max_length=255,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
            }
        )
    )
    abstract = True


# User Registration form
class RegistrationForm(BaseForm):
    """The User Registration form"""
    email = forms.CharField(
        max_length=255,
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
            }
        )
    )

    password2 = forms.CharField(
        max_length=255,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
            }
        )
    )


# User Login Form
class LoginForm(BaseForm):
    """The User Login form"""


# CONTACT FORM
class ContactMeForm(forms.Form):
    name = forms.CharField(
        max_length=200,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            }
        )
    )

    email = forms.CharField(
        max_length=200,
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
            }
        )
    )

    subject = forms.CharField(
        max_length=200,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            }
        )
    )

    text = forms.CharField(
        required=True,
        widget=forms.Textarea(
            attrs={
                'class': "form-control",
                'rows': 3,
            }
        )
    )


