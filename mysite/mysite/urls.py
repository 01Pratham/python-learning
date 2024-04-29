"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from home.views import *
from home.resources import MyModelListView
from home.resources import deleteProfile
from home.resources import LoginView

urlpatterns = [
    path ('',home),
    path('another',another_route),
    path('admin/', admin.site.urls),
    path('userreg/', userreg),
    path('insertuser', insertuser),
    path('viewuser', viewuser),
    path('deleteprofile/<int:id>', deleteprofile),
    path('mymodel/', MyModelListView.as_view()),
    path('delete/<int:id>', deleteProfile.as_view()),
    path('login/', LoginView.as_view()),


]