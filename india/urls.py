from india.views import *
from django.urls import path

app_name='virat'

urlpatterns=[
    path('rohit/',rohit,name='rohit'),
    path('virat/',virat,name='virat')
]