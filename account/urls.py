from django.urls import path, re_path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns=[

    re_path(r'^login/$', auth_views.login, name='login'),
    re_path(r'^logout/$', auth_views.logout, name='logout'),
    re_path(r'^logout-then-login/$', auth_views.logout_then_login, name='logout_then_login'),
    re_path(r'^$', views.dashboard, name='dashboard'),
    re_path(r'^password-change/$', auth_views.password_change, name='password_change'),
    re_path(r'^password-change/done/$', auth_views.password_change_done, name='password_change_done'),
    re_path(r'^password-reset/$', auth_views.password_reset, name="password_reset"),
    re_path(r'^password-reset/done/$', auth_views.password_reset_done, name="password_reset_done"),
    re_path(r'^password-reset/confirm/(?P<uidb64>[-\w]+)/(?P<token>[-\w]+)/$',
            auth_views.password_reset_confirm, name="password_reset_confirm"),
    re_path(r'^password-reset/complete/$', auth_views.password_reset_complete, name="password_reset_complete"),
    re_path(r'^register/$', views.register, name='register'),
    re_path(r'^edit/$', views.edit, name='edit'),

]


