from django.urls import path
from django.urls import path,include
from . import views

urlpatterns = [

    #HOME
    path('',views.home,name='home'),
    path('register',views.poster_register,name='poster_register'),

    #DASHBOARD
    path('login',views.login,name="login"),
    path('dashboard',views.dashboard,name='dashboard'),
    path('accounts',views.acounts,name="acounts"),
    path('contents',views.contents,name="contents"),

    #CONTENTS
    path('contents/save',views.save_content),
]