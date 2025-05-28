from django.utils.translation import gettext_lazy as _

# School Years
SCHOOL_YEARS = [
    ('7', 'Year 7'),
    ('8', 'Year 8'),
    ('9', 'Year 9'),
    ('10', 'Year 10'),
    ('11', 'Year 11'),
]

# Difficulty Levels
DIFFICULTY_CHOICES = [
    ('EASY', _('Easy')),
    ('MEDIUM', _('Medium')),
    ('HARD', _('Hard')),
]

# Topics
TOPIC_CHOICES = [
    ('ALGEBRA', _('Algebra')),
    ('GEOMETRY', _('Geometry')),
    ('NUMBER', _('Number')),
    ('STATISTICS', _('Statistics')),
    ('PROBABILITY', _('Probability')),
]

# Number of Questions
QUESTION_COUNT_CHOICES = [
    ('5', '5 Questions'),
    ('10', '10 Questions'),
    ('15', '15 Questions'),
    ('20', '20 Questions'),
] 