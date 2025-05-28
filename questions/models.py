from django.db import models
from .constants import DIFFICULTY_CHOICES, TOPIC_CHOICES, SCHOOL_YEARS

class QuestionSet(models.Model):
    name = models.CharField(max_length=200)
    year = models.CharField(max_length=2, choices=SCHOOL_YEARS)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name} ({self.year})"

class MathQuestion(models.Model):
    question_text = models.TextField()
    choice_a = models.CharField(max_length=100)
    choice_b = models.CharField(max_length=100)
    choice_c = models.CharField(max_length=100)
    choice_d = models.CharField(max_length=100)
    correct_answer = models.CharField(max_length=1, choices=[('A','A'),('B','B'),('C','C'),('D','D')])
    topic = models.CharField(max_length=20, choices=TOPIC_CHOICES)
    difficulty = models.CharField(max_length=10, choices=DIFFICULTY_CHOICES)
    school_year = models.CharField(max_length=2, choices=SCHOOL_YEARS)
    question_sets = models.ManyToManyField(QuestionSet, related_name='questions', blank=True)

    def __str__(self):
        return self.question_text[:50]
