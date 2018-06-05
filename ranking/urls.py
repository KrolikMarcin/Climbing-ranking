from django.urls import path, re_path
from . import views


urlpatterns = [

    path('', views.ranking, name='ranking'),
    re_path(r'^(?P<pk>[0-9]+)/$', views.ascents, name='ascents'),

    path('new-ascent/', views.new_ascent, name='new_ascent'),
    # path('seniors_m/', views.seniors_m, name='category'),
    # path('seniors_w/', views.seniors_w, name='category'),
    # path('juniors_m/', views.juniors_m, name='category'),
    # path('juniors_w/', views.juniors_w, name='category'),

    path('category/<str:category>', views.category, name='category'),
    re_path(r'^logged_user/$', views.ascents_logged_user, name='ascents_logged_user'),
    re_path(r'^ascent-edit/(?P<pk>[0-9]+)/$', views.ascent_edit, name='ascent_edit'),


]
