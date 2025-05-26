from django.urls import path
from . import views

urlpatterns = [
    path('', views.question_list, name='question_list'),
    path('<int:pk>/', views.question_detail, name='question_detail'),
    path('<int:pk>/check/<str:choice>/', views.check_answer, name='check_answer'),
]
