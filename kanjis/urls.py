from django.urls import path
from . import views

urlpatterns = [
    path('', views.lander, name='lander'),
    path('data/', views.data, name='data'),
    path('quiz/',views.quiz, name='quiz'),
    path('quiz/jlpt/n<int:jlptlevel>/',views.quiz_jlpt, name='quiz_jlpt'),
    path('quiz/rkmath/<str:course>/',views.quiz_rkmath, name='quiz_rkmath'),
    path('quiz/jaltap/<int:chapter>/',views.quiz_jaltap, name="quiz_jaltap"),
    path('quiz/soumatome/n<int:jlptlevel>/<int:chapter>/',views.quiz_somatome, name='quiz_somatome')
]