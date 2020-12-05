from django.urls import path

from . import views

urlpatterns = [
    path('country_list', views.country_list),
    path('get_started', views.get_started),
    path('<str:country>', views.country),
    path('create/', views.create_db),
    path('update/', views.update_db)
]