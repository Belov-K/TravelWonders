from django.urls import path

from . import views

app_name='tours'
urlpatterns=[
    path('', views.hotel_list, name='hotel_list'),
    path('tour/', views.tour_list, name='tour_list')
]