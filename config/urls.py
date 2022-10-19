"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from skil import views as skil_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('skil/', include('skil.urls')),
    path('skil/wordtest/', include('skil.urls')),
    path('skil/exceltest/', include('skil.urls')),
    path('skil/wordtest/wordanswer/', include('skil.urls')),
    path('skil/exceltest/excelanswer/', include('skil.urls')),
    path('skil/percent/', include('skil.urls')),
]
