from django.urls import path
from . import views


app_name = 'lookup'

urlpatterns = [
    path('', views.home_view, name='home'),
    path('about/', views.AboutView.as_view(), name='about')

]
