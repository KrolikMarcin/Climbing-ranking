from django.urls import path, re_path
from . import views


urlpatterns = [

    path('', views.ranking, name='ranking'),
    path('category/<str:category>/', views.category, name='category'),

]
