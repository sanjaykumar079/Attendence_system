
from django.contrib import admin
from django.urls import path

from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('nav', views.nav, name='nav'),
    path('attendance_upload/', views.upload_attendance, name='attendance_upload'),
    path('view/', views.view_attendance, name='view_attendance'),
    path('', views.home, name='home'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('attendance_upload_success', views.attendance_upload_success, name='attendance_upload_success'),

]
