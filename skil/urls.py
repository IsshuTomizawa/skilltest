from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('nsele/', views.nsele, name='NS'),
    path('esele/', views.esele, name='ES'),
    path('<int:net_id>/nettest/', views.nettest, name='NT'),
    path('<int:excel_id>/exceltest/', views.exceltest, name='ET'),
    path('<int:net_id>/Nanswer/', views.Nanswer, name='Nanswer'),
    path('<int:excel_id>/Eanswer/', views.Eanswer, name='Eanswer'),
    path('percent/', views.percent, name='percent'),
]