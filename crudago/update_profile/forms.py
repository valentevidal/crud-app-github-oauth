from django.forms import ModelForm, DateInput

from django.db import models as db_models
from update_profile.models import UserProfile
from django.contrib.auth.models import User
from crispy_forms.helper import FormHelper




class UserForm(ModelForm):

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')
        label = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'email': 'Email',
        }


class ProfileForm(ModelForm):

    class Meta:
        model = UserProfile
        fields = ('address_1', 'address_2', 'phone_number', 'birthday', 'gender')
        widgets = {
        'birthday': DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
    }



