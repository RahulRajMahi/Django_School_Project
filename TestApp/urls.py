from django.contrib import admin
from django.urls import path
from TestApp import views

urlpatterns = [
    path('', views.view_home),
    path('student/', views.view_student),
    path('teacher/', views.view_teacher),
    path('book/', views.view_book),
]
