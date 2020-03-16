from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .forms import UserForm, ProfileForm
from django.views.generic import UpdateView
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.forms import AdminPasswordChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages






@login_required
def home(request):
    print ("HOME")
    return render(request, 'update_profile/home.html')

@login_required
def logout_redirect(request):
    return render(request, 'registration/logout_redirect.html')

@login_required
def profile_form(request):

    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.userprofile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return HttpResponseRedirect('/')


    user_form = UserForm(initial={'first_name': request.user.first_name,
                                  'last_name': request.user.last_name,
                                  'username': request.user.username
                                  })
    profile_form = ProfileForm(initial={'address_1': request.user.userprofile.address_1,
                                        'address_2': request.user.userprofile.address_2,
                                        'phone_number': request.user.userprofile.phone_number,
                                        'birthday': request.user.userprofile.birthday,
                                        'gender': request.user.userprofile.gender,
    })
    return render(request, 'update_profile/profile_form.html', {'user_form': user_form, 'profile_form': profile_form} )

@login_required
def delete_user(request):
    if request.method == 'POST':
        uid = request.user.id
        User.objects.filter(id=uid).delete()
        return HttpResponseRedirect('/')

@login_required
def change_password(request):
    if request.user.has_usable_password():
        PasswordForm = PasswordChangeForm
    else:
        PasswordForm = AdminPasswordChangeForm
    if request.method == 'POST':
        form = PasswordForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, 'Your password was successfully updated!')
            return HttpResponseRedirect('/')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordForm(request.user)
    return render(request, 'registration/change_password.html', {'form': form })