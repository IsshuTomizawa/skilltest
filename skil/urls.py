from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('nettest/', views.nettest, name='NT'),
    path('exceltest/', views.exceltest, name='ET'),
    path('Nanswer/', views.Nanswer, name='Nanswer'),
    path('Eanswer/', views.Eanswer, name='Eanswer'),
    path('parcent/', views.percent, name='percent'),
]