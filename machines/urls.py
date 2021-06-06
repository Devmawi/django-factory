from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id>/', views.details, name='details'),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('create/', views.create, name='create'),
]