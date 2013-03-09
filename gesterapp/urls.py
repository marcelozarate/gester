# -*- coding: utf-8 *-*

from django.conf.urls import patterns, url

urlpatterns = patterns('gesterapp.views',
    url(r'^$', 'home', name='home'),
    url(r'^about/$', 'about', name='about'),
    url(r'^add-user/$', 'add_user', name='add-user'),
    url(r'^add-mate/$', 'add_mate', name='add-mate'),
    url(r'^add-termo/$', 'add_termo', name='add-termo'),
    url(r'^add-bombilla/$', 'add_bombilla', name='add-bombilla'),
    url(r'^add-prestamo/$', 'add_prestamo', name='add-prestamo'),
    url(r'^list-users/$', 'list_users', name='list-users'),
    url(r'^list-mates/$', 'list_mates', name='list-mates'),
    url(r'^list-termos/$', 'list_termos', name='list-termos'),
    url(r'^list-bombillas/$', 'list_bombillas', name='list-bombillas'),
    url(r'^list-prestamos/$', 'list_prestamos', name='list-prestamos'),
    url(r'^prestar/$', 'prestar', name='prestar'),
    url(r'^get_usuarios/', 'get_usuarios', name='get_usuarios'),
)
