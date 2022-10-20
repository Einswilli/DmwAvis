from django.urls import path
from django.urls import path,include
from . import views

urlpatterns = [

    #HOME
    path('',views.home,name='home'),
]