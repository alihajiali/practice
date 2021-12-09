from django import forms
from django.forms.widgets import PasswordInput, TextInput


class login_form(forms.Form):
    username = forms.CharField(label='username', max_length=30, widget=forms.TextInput(
        attrs={"style": "background-color:transparent;color: white; border-top: 0;border-right: 0;border-left:0;border-color: white; "}))
    password = forms.CharField(label='password', max_length=50, widget=forms.PasswordInput(
        attrs={"style": "background-color:transparent;color: white; border-top: 0;border-right: 0;border-left:0;border-color: white;"}))


class register_form(forms.Form):
    username = forms.CharField(label='username', max_length=30, widget=forms.TextInput(
        attrs={"style": "background-color:transparent;color: white; border-top: 0;border-right: 0;border-left:0;border-color: white; "}))
    email = forms.EmailField(label='email', max_length=100, widget=forms.TextInput(
        attrs={"style": "background-color:transparent;color: white; border-top: 0;border-right: 0;border-left:0;border-color: white;"}))
    password = forms.CharField(label='password', max_length=50, widget=forms.PasswordInput(
        attrs={"style": "background-color:transparent;color: white; border-top: 0;border-right: 0;border-left:0;border-color: white;"}))
