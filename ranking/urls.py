from django.urls import path, re_path
from . import views


urlpatterns = [

    path('', views.ranking, name='ranking'),
    re_path(r'^(?P<pk>[0-9]+)/$', views.ascents, name='ascents'),
    path('new-ascent/', views.new_ascent, name='new_ascent'),
    path('category/<str:category>/', views.category, name='category'),
    re_path(r'^ascent-edit/(?P<pk>[0-9]+)/$', views.ascent_edit, name='ascent_edit'),


]
