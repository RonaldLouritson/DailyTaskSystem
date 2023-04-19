from django.urls import path
from . import views

from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('', views.home, name='home'),
    path('<int:pk>/', views.job_issue, name='job_issue'),
    path('<int:pk>/create/', views.create_job_issue, name='create_job_issue'),
    path('<int:pk>/delete/<int:job_pk>/', views.delete_job_issue, name='delete_job_issue'),
    path('<int:pk>/edit/<int:job_pk>/', views.edit_job_issue, name='edit_job_issue'),
    path('<int:pk>/edit/<int:job_pk>/delete_note/<int:note_pk>/', views.delete_note, name='delete_note'),
]