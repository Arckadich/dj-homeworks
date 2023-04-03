"""first_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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

from app.views import home_view

from django.urls import include, path
from . import views
from .views import HomeView

urlpatterns = [
    path('', views.home, name='home'),
]
# В этом примере шаблон URL '' (пустая строка) сопоставляется с домашней функцией в модуле view.


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
]
# В этом примере шаблон URL '' (пустая строка) сопоставляется с представлением на основе класса HomeView.
# Метод as_view() вызывается для создания экземпляра класса представления, который может обрабатывать запрос.



urlpatterns = [
    path('blog/', include('blog.urls')),
]
#В этом примере функция include() используется для включения конфигурации URL для приложения блога.
# Любые URL-адреса, начинающиеся с blog/, будут обрабатываться URLconf в приложении блога.



from django.urls import path
from .views import time_view, workdir_view
from django.contrib import admin

urlpatterns = [
    path('current_time/', time_view, name='time'),
    path('workdir/', workdir_view, name='workdir'),
    path('admin/', admin.site.urls),
]
