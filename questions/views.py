from django.shortcuts import render, get_object_or_404
from .models import MathQuestion
from django.http import HttpResponse

def question_list(request):
    # Get filter parameters
    selected_year = request.GET.get('year')
    selected_topic = request.GET.get('topic')
    
    # Base queryset
    questions = MathQuestion.objects.all()
    
    # Apply filters if provided
    if selected_year:
        questions = questions.filter(school_year=selected_year)
    if selected_topic:
        questions = questions.filter(topic=selected_topic)
    
    # Get unique years and topics for filter dropdowns
    years = MathQuestion.objects.values_list('school_year', flat=True).distinct().order_by('school_year')
    topics = [choice[0] for choice in MathQuestion.TOPIC_CHOICES]
    
    context = {
        'questions': questions,
        'years': years,
        'topics': topics,
        'selected_year': selected_year,
        'selected_topic': selected_topic,
    }
    
    # If this is an HTMX request, return only the table
    if request.headers.get('HX-Request'):
        return render(request, 'questions/question_table.html', context)
    
    return render(request, 'questions/question_list.html', context)

def question_detail(request, pk):
    question = get_object_or_404(MathQuestion, pk=pk)
    return render(request, 'questions/question_detail.html', {'question': question})

def check_answer(request, pk, choice):
    question = get_object_or_404(MathQuestion, pk=pk)
    is_correct = choice == question.correct_answer
    
    if is_correct:
        return HttpResponse('<div class="card shadow-sm"><div class="card-body text-center"><h4 class="mb-0 text-success">✓ Correct!</h4></div></div>')
    else:
        return HttpResponse('<div class="card shadow-sm"><div class="card-body text-center"><h4 class="mb-0 text-danger">✗ Incorrect</h4></div></div>')
