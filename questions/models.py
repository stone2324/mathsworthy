from django.db import models

class MathQuestion(models.Model):
    DIFFICULTY_CHOICES = [
        ('EASY', 'Easy'),
        ('MEDIUM', 'Medium'),
        ('HARD', 'Hard'),
    ]

    TOPIC_CHOICES = [
        ('ALGEBRA', 'Algebra'),
        ('GEOMETRY', 'Geometry'),
        ('CALCULUS', 'Calculus'),
        ('STATISTICS', 'Statistics'),
        ('TRIGONOMETRY', 'Trigonometry'),
        ('ARITHMETIC', 'Arithmetic'),
    ]

    question_text = models.TextField()
    choice_a = models.CharField(max_length=100)
    choice_b = models.CharField(max_length=100)
    choice_c = models.CharField(max_length=100)
    choice_d = models.CharField(max_length=100)
    correct_answer = models.CharField(max_length=1, choices=[('A','A'),('B','B'),('C','C'),('D','D')])
    topic = models.CharField(max_length=20, choices=TOPIC_CHOICES)
    difficulty = models.CharField(max_length=10, choices=DIFFICULTY_CHOICES)
    school_year = models.IntegerField()

    def __str__(self):
        return self.question_text[:50]
