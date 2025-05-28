from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path('questions/', views.question_list, name='question_list'),
    path('questions/<int:pk>/', views.question_detail, name='question_detail'),
    path('questions/<int:pk>/check/<str:choice>/', views.check_answer, name='check_answer'),
    path('check-answer/<int:question_id>/', views.check_answer, name='check_answer'),
    path('daily-challenges/', views.daily_challenges, name='daily_challenges'),
    path('create-question-set/', views.create_question_set, name='create_question_set'),
    path('view-question-set/<int:set_id>/', views.view_question_set, name='view_question_set'),
    path('api/matching-questions/', views.get_matching_questions, name='get_matching_questions'),
]
