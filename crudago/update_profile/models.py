from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField


gender_options = [
    ("women", "Women"),
    ("men", "Men"),
    ("unspecified", "Unspecified"),
    ("other", "Other / I rather not say"),
]

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address_1 = models.CharField(max_length=200, blank=False,)
    address_2 = models.CharField(max_length=200, blank=False,)
    # https://github.com/stefanfoulis/django-phonenumber-field
    phone_number = PhoneNumberField()
    birthday = models.DateField(blank=False)
    gender = models.CharField(max_length=200, choices=gender_options, blank=False)