from django import forms
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.forms import AuthenticationForm, UsernameField

class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={"autofocus": True,'class':'form-control','placeholder':'Username'}))
    password = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "current-password",'class':'form-control','placeholder':'Password'}),
    )
    
    def username_clean(self):
        username = self.cleaned_data.get("username")
        if username.isalpha():
            return username
        else:
            raise forms.ValidationError("Username Can Not Contain numbers")