from django import forms
from django.forms.models import ModelForm

from .models import CustomUser


class LoginForm(forms.Form):
    email = forms.CharField(max_length=63)
    password = forms.CharField(max_length=63, widget=forms.PasswordInput)


class SignUpForm(ModelForm):
    password = forms.CharField(
        max_length=128, min_length=8, widget=forms.PasswordInput(), label="Password")
    confirm_password = forms.CharField(
        max_length=128, min_length=8, widget=forms.PasswordInput(), label="Verify Password")

    class Meta:
        model = CustomUser
        fields = ['email', 'phoneNo', 'password']

    def clean(self):
        cleaned_data = super(SignUpForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            self.add_error('confirm_password', "Password does not match")
            raise forms.ValidationError(
                "password and confirm_password does not match"
            )
