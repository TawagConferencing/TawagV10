from django.urls import path
from . import views
#defining the html here in urls.py
urlpatterns = [
    path('register/',views.register, name='register'),
    path('login/',views.login_view, name='login'),
    path('dashboard/',views.dashboard, name='dashboard'),
    path('logout/',views.login_view, name='logout'),
    path('meeting/',views.newmeeting, name='meeting'),
    path('room/',views.joinroom,name='room'),
    path('',views.index, name='index'),
    
]