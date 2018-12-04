from django.urls import path
from . import views


app_name = 'hw1'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:person_id>/', views.detail, name='detail'),
    path('registration/', views.registration, name='registration'),
    path('<int:person_id>/action/', views.action, name='action'),
]

