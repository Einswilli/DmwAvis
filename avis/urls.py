from django.urls import path
from django.urls import path,include
from . import views

urlpatterns = [

    #HOME
    path('',views.home,name='home'),
    path('register',views.poster_register,name='poster_register'),

    #DASHBOARD
    path('login',views.login,name="login"),
    path('logout',views.logout,name="logout"),
    path('dashboard',views.dashboard,name='dashboard'),
    path('accounts',views.acounts,name="accounts"),
    path('contents',views.contents,name="contents"),
    path('posts',views.posts,name="posts"),

    #CONTENTS
    path('contents/save',views.save_content),
    path('contents/add/',views.assign_content),

    #ACCOUNTS
    path('accounts/save',views.account_save),
    path('account/add/',views.assign_account),

    #POSTS
    path('posts/save',views.save_post),
    path('posts/validate/<int:id>',views.validate_post),
    path('posts/reject/<int:id>',views.reject_post),

    #USERS
    path('users/save', views.save_user, name='usersave'),
]