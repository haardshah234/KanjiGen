from django.urls import path
from . import views

urlpatterns = [
    path('', views.lander, name='lander'),
    path('data/', views.data, name='data'),
    path('quiz/',views.quiz, name='quiz'),
]