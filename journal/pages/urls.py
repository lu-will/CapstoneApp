from django.urls import path
from . import views

app_name = 'pages'
urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register, name='register'),
    path('day/', views.dayview, name='day'),
    path('saveday/', views.savedayview, name='saveday'),
    path('evening/', views.eveningview, name='evening'),
    path('saveevening/', views.saveeveningview, name='saveevening'),
    path('<str:username>/', views.userposts, name='userposts'),

]