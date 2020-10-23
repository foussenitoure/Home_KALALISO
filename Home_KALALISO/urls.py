"""Home_KALALISO URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from kalaliso import views

urlpatterns = [
    url(r'', admin.site.urls),
    # url('admin/', admin.site.urls),
    # url(r'^$', views.look, name='home'),
    url(r'^home/$', views.look, name='home'),
    url(r'^index/$', views.indexpage, name='indexpage'),
    # url(r'', views.indexpage, name='indexpage'),
    # url(r'^newPage/$', views.newPage, name='newPage'),
    url(r'^thanks/$', views.thanks, name='thanks'),
    url(r'^getformdata/$', views.get_form_data, name='get-form-data'),
    # url(r'^getperson/$', views.list_person, name='list_personnes'),
    url(r'^getperson/$', views.list_person, name='list_personnes'),
    # url(r'^merci/$', views.merci, name='merci'),
    url(r'^mesure/$', views.mesure_client, name='get-mesure-client'),
    url(r'^depense/$', views.depenses, name='get-depense'),
    url(r'^commande/$', views.new_command, name='get-commande'),
    url(r'^commande_detail/$', views.commande_details, name='get-commande-detail'),
    # url(r'^mesure/$', views.mesure_data, name='get-mesure-data'),
    # url(r'^users_detail/$', views.users_detail, name='users_detail'),

]
