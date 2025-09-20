from django.urls import path
from . import views

urlpatterns = [
    path('', views.people_list, name='people_list'),
    path('people/<int:pk>/', views.people_detail, name='people_detail'),
    path('people/new/', views.people_create, name='people_create'),
    path('people/<int:pk>/edit/', views.people_edit, name='people_edit'),
    path('people/<int:pk>/delete/', views.people_delete, name='people_delete'),
]