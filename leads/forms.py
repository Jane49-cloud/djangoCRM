from django import forms
from .models import Lead
from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.contrib.auth import get_user_model


User = get_user_model


class LeadModelForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = [
            'first_name',
            'last_name',
            'age',
            'phoned',
            'source',
            'profile_picture',
            'special_files',
            'agent',
            'cellphone',
            'email'
        ]


class UserCustomForm(UserCreationForm):
    class meta:
        model = User
        fields = "username"
        field_classes = ("username", UsernameField)

        # class LeadForm(forms.Form):
        #     first_name = forms.CharField()
        #     last_name = forms.CharField()
        #     age_ = forms.IntegerField()
