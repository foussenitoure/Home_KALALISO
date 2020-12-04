
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
    url(r'^person/$', views.get_person, name='get-person'),
    # url(r'^getperson/$', views.list_person, name='list_personnes'),
    url(r'^getperson/$', views.list_person, name='list_personnes'),
    # url(r'^merci/$', views.merci, name='merci'),
    url(r'^produit/$', views.product, name='get-product'),
    url(r'^mesure/$', views.mesure_client, name='get-mesure'),
    url(r'^depense/$', views.depenses, name='get-depense'),
    url(r'^depense_detail/$', views.depenses_detail, name='get-depense-detail'),
    url(r'^commande/$', views.new_command, name='get-commande'),
    url(r'^commande_detail/$', views.commande_details, name='get-commande-detail'),

    # url(r'^users_detail/$', views.users_detail, name='users_detail'),

]
