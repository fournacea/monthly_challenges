from django.urls import path
from . import views


urlpatterns = [
    path('index', views.index),
    path('january', views.january),
    path('february', views.february),
    path('march', views.march),
    path('april', views.april),

]
