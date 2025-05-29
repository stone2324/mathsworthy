from django.shortcuts import render, get_object_or_404, redirect
from .models import MathQuestion, QuestionSet
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.contrib import messages
from .constants import SCHOOL_YEARS, DIFFICULTY_CHOICES, TOPIC_CHOICES, QUESTION_COUNT_CHOICES
import json

def landing_page(request):
    if request.user.is_authenticated:
        return redirect('question_list')
    return render(request, 'questions/landing_page.html')

@login_required(login_url='/accounts/login/')
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
    topics = [choice[0] for choice in TOPIC_CHOICES]
    
    # Pagination
    paginator = Paginator(questions, 10)  # Show 10 questions per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'page_obj': page_obj,
        'years': years,
        'topics': topics,
        'selected_year': selected_year,
        'selected_topic': selected_topic,
    }
    
    # If this is an HTMX request, return only the table
    if request.headers.get('HX-Request'):
        return render(request, 'questions/questions/question_table.html', context)
    
    return render(request, 'questions/questions/question_list.html', context)

@login_required(login_url='/accounts/login/')
def question_detail(request, pk):
    question = get_object_or_404(MathQuestion, pk=pk)
    return render(request, 'questions/questions/question_detail.html', {'question': question})

@login_required(login_url='/accounts/login/')
def check_answer(request, pk, choice):
    question = get_object_or_404(MathQuestion, pk=pk)
    is_correct = choice == question.correct_answer
    
    if is_correct:
        return HttpResponse('<div class="card shadow-sm"><div class="card-body text-center"><h4 class="mb-0 text-success">✓ Correct!</h4></div></div>')
    else:
        return HttpResponse('<div class="card shadow-sm"><div class="card-body text-center"><h4 class="mb-0 text-danger">✗ Incorrect</h4></div></div>')

@login_required
def daily_challenges(request):
    question_sets = QuestionSet.objects.all().order_by('-created_at')
    return render(request, 'questions/challenges/daily_challenges.html', {
        'question_sets': question_sets,
        'school_years': SCHOOL_YEARS,
        'difficulty_choices': DIFFICULTY_CHOICES,
        'topic_choices': TOPIC_CHOICES,
        'question_count_choices': QUESTION_COUNT_CHOICES
    })

@login_required
def create_question_set(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        year = request.POST.get('year')
        selected_topics = request.POST.getlist('topics')
        difficulty = request.POST.get('difficulty')

        # Create the question set
        question_set = QuestionSet.objects.create(
            name=name,
            year=year
        )

        # Find matching questions and add them to the set
        questions = MathQuestion.objects.filter(
            school_year=year,
            topic__in=selected_topics,
            difficulty=difficulty
        )
        question_set.questions.add(*questions)

        messages.success(request, 'Question set created successfully!')
        return redirect('daily_challenges')
    
    return redirect('daily_challenges')


@login_required
def view_question_set(request, set_id):
    question_set = get_object_or_404(QuestionSet, id=set_id)
    questions = question_set.questions.all()
    
    return render(request, 'questions/challenges/view_question_set.html', {
        'question_set': question_set,
        'questions': questions
    })

@login_required
def get_matching_questions(request):
    year = request.GET.get('year')
    difficulty = request.GET.get('difficulty')
    topics = request.GET.get('topics', '').split(',')
    
    questions = MathQuestion.objects.filter(
        school_year=year,
        difficulty=difficulty,
        topic__in=topics
    )
    
    questions_data = [{
        'text': q.text,
        'topic': q.get_topic_display(),
        'difficulty': q.get_difficulty_display()
    } for q in questions]
    
    return JsonResponse({
        'questions': questions_data,
        'count': questions.count()
    })
