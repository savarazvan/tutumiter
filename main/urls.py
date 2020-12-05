from django.urls import path

from . import views

urlpatterns = [
    path('country_list', views.country_list),
    path('get_started', views.get_started),
    path('country', views.country),
    path('update/', views.update_db)
]