
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from update_profile import views as up_views


urlpatterns = [

    path('admin/', admin.site.urls),
    path('', up_views.home, name='home'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('logout_redirect/', up_views.logout_redirect, name='logout_redirect'),
    path('oauth/', include('social_django.urls', namespace='social')), 
    path('profile_form/', up_views.profile_form, name='profile_form' ),
    path('delete_user/', up_views.delete_user, name='delete_user')

]

