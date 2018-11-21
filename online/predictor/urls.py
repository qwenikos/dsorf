from django.urls import path

from . import views

urlpatterns = [
    path('input_form/', views.input_form,name='input_form'),
    path('results/', views.results),
    path('',views.index,name='index'),
    path('help/',views.help,name='help'),
    path('download/',views.download,name='download'),
    ]

