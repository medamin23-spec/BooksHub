from django.shortcuts import render, redirect
from .models import Book
from .forms import LoginForm, RegisterForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def login_view(req):
    if req.method == 'POST':
        form = LoginForm(req.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user:
                login(req, user)
                return redirect('home')
    else:
        form = LoginForm()
    return render(req, 'accounts/login.html', {'form': form})
def register_view(req):
    if req.method == 'POST':
        form = RegisterForm(req.POST)
        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data.get('password')
            user.set_password(password)
            user.save()
            login(req, user)
            return redirect('home')
    else:
        form = RegisterForm()
    return render(req, 'accounts/register.html', {'form': form})
@login_required
def home(req):
    books = Book.objects.all()
    context = {
        'books': books,
    }
    return render(req, 'Home_Page/home.html', context)
