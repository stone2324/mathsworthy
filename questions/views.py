from django.shortcuts import render, get_object_or_404
from .models import MathQuestion

def question_list(request):
    questions = MathQuestion.objects.all()
    return render(request, 'questions/question_list.html', {'questions': questions})

def question_detail(request, pk):
    question = get_object_or_404(MathQuestion, pk=pk)
    return render(request, 'questions/question_detail.html', {'question': question})
