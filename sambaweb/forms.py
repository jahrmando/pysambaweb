# -*- encoding: utf-8 -*-
from django import forms


class UserForm(forms.Form):
    nickname = forms.RegexField(
        min_length=2,
        required=True,
        regex=r'^[a-zA-Z0-9_]+$',
        widget=forms.TextInput(attrs={
            'id': 'nickname',
            'name': 'nickname'
        })
    )
    oldpasswd = forms.RegexField(
        min_length=10,
        required=True,
        regex=r'^[a-zA-Z0-9_]+$',
        widget=forms.PasswordInput(attrs={
            'id': 'oldpasswd',
            'name': 'oldpasswd'
        })
    )
    newpasswd = forms.RegexField(
        min_length=10,
        required=True,
        regex=r'^[a-zA-Z0-9_]+$',
        widget=forms.PasswordInput(attrs={
            'id': 'newpasswd',
            'name': 'newpasswd'
        })
    )
    retpasswd = forms.RegexField(
        min_length=10,
        required=True,
        regex=r'^[a-zA-Z0-9_]+$',
        widget=forms.PasswordInput(attrs={
            'id': 'retpasswd',
            'name': 'retpasswd'
        })
    )
