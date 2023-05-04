from django.urls import path
from . import views


urlpatterns = [
    path('index', views.index, name='index'),
    path('january', views.january, name='janurary'),
    path('february', views.february, name='february'),
    path('march', views.march, name='march'),
    path('april', views.april, name='april'),
    path('<month>', views.monthly_challenge, name='monthly_challenge')

]
