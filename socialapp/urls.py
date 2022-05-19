from django.urls import re_path as url
from django.urls import include
from . import views as v
from django.urls import path,include
urlpatterns = [

    path('',v.home,name='home'),
    path('signin',v.signin,name='signin')



]
