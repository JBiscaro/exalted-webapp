"""exalted_webapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from calculator import views

urlpatterns = [
    path('', views.index, name='home'),
    path('admin/', admin.site.urls),
    path('results/', views.results, name='results'),
    path(r'charms/<slug>/edit/', views.edit_charm, name='edit_charm'),
    path('selected_charms', views.selected_charms, name='selected_charms'),
    path('reset', views.reset, name='reset'),
    path('charms/brawl', views.brawl, name='brawl'),
    path('charms/athletics', views.athletics, name='athletics'),
    path('charms/occult', views.occult, name='occult'),
    path('charms/resistance', views.resistance, name='resistance'),
    path('charms/evocations', views.evocations, name='evocations'),
    path(r'charms/<slug>/activate', views.activate_charm, name='activate_charm'),
    path(r'charms/<slug>/deactivate', views.deactivate_charm, name='deactivate_charm'),
]
