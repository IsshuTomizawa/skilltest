from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('wordtest/', views.wordtest, name='WT'),
    path('exceltest/', views.exceltest, name='ET'),
    path('percent/', views.percent, name='percent'),
]