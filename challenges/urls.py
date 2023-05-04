from django.urls import path
from . import views


urlpatterns = [
    path('index', views.index, name='index'),
    path('january', views.january, name='janurary'),
    path('february', views.february, name='february'),
    path('march', views.march, name='march'),
    path('april', views.april, name='april'),
    path('<str:month>', views.monthly_challenge, name='monthly_challenge'),
    path('month_num/<int:month_num>', views.monthly_challenge_by_number, name='monthly_challenge_by_number'),

]
