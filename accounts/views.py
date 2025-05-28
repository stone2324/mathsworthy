from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.views import LoginView
from django.urls import reverse
from .forms import UserRegistrationForm, UserProfileForm

class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'
    redirect_authenticated_user = True
    success_url = 'question_list'

    def form_invalid(self, form):
        if '__all__' in form._errors and form._errors['__all__'] == ['Please enter a correct username and password. Note that both fields may be case-sensitive.']:
            form._errors['__all__'] = ['Invalid username or password. Please try again.']
        return super().form_invalid(form)

# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration successful!')
            return redirect('profile')
    else:
        form = UserRegistrationForm()
    return render(request, 'accounts/register.html', {'form': form})

@login_required
def profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=request.user.userprofile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your preferences have been updated!')
            return redirect('profile')
    else:
        form = UserProfileForm(instance=request.user.userprofile)
    return render(request, 'accounts/profile.html', {'form': form})

def htmx_logout(request):
    if request.method == 'POST':
        logout(request)
        if request.headers.get('HX-Request'):
            return HttpResponse('''
                <div hx-get="/login-required/" hx-trigger="load" hx-push-url="true"></div>
            ''')
        return redirect('login_required')
    return HttpResponse(status=405)  # Method Not Allowed
