from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('listings', views.listings, name='listings'),
    path('details', views.details, name='details'),
]
