from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField


gender_options = [
    ("female", "Female"),
    ("male", "Male"),
    ("unspecified", "Unspecified"),
    ("other", "Other / I rather not say"),
]

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address_1 = models.CharField(max_length=200, blank=False, null=True)
    address_2 = models.CharField(max_length=200, blank=False, null=True)
    # https://github.com/stefanfoulis/django-phonenumber-field
    phone_number = PhoneNumberField()
    birthday = models.DateField(blank=False, null=True)
    gender = models.CharField(max_length=200, choices=gender_options, blank=False, null=True)






def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

post_save.connect(create_user_profile, sender=User)