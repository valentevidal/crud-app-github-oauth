from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render
from .forms import UserForm, ProfileForm
from django.views.generic import UpdateView
from django.http import HttpResponse, HttpResponseRedirect


def home(request):
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
        print (uid)
        User.objects.filter(id=uid).delete()
        return render(request, '') 