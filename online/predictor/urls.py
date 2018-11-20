from django.urls import path

from . import views

urlpatterns = [
    #path('', views.index, name='index'),

    path('input_form/', views.input_form,name='input_form'),
    path('results/', views.results),
    #path('index/',views.index),
    path('',views.index,name='index'),
    # path('dsorf_output/','dsorf_output/','dsorf_output/'),
    ]

