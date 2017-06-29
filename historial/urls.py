"""untitled URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() func    tion: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
#from django.conf.urls import patterns
from dal import autocomplete
from django.conf.urls import url
from registrar import views
from django.contrib import admin
from .views import about
from registrar.autocomplete import PersonaAutocomplete
from django.views.generic.base import RedirectView


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r'^$', views.inicio, name='inicio'),
    url(r'^$', RedirectView.as_view(url='/admin')),

    url(r'^login/$', views.login, name='login'),
    url(r'^contacto/$', views.login, name='contacto'),
    url(r'^about/$', about, name='about'),
    url(r'^registrar/$', about, name='registrar'),
    # url(r'autocomplete/', include('autocomplete_light.urls')),
    url(
        r'^persona-autocomplete/$',
        PersonaAutocomplete.as_view(),
        name='persona-autocomplete',
    ),
]
