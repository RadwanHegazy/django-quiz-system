from django.urls import path
from .views import GET, login_POST, register_POST
from django.contrib.auth.views import LogoutView

urlpatterns = [

    path('',GET.view_auth_template,name='user_auth'),
    
    path('login/',login_POST.login,name='login'),
    path('register/',register_POST.register,name='register'),

    path('logout/',LogoutView.as_view(),name='logout'),

]