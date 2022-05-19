from django.urls import re_path as url
from django.urls import include
from . import views as v
urlpatterns = [

    url('',v.home,name='home')
]
