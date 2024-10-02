from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from griffin.models import Project  # Import Project model from the Griffin app
from django.contrib import messages
from django.views.decorators.cache import never_cache  # Import never_cache

# View function to render the index page (public)
def index(request):
    return render(request, 'base/index.html')

# View function to render the homepage (restricted to authenticated users)
@login_required(login_url='login')
@never_cache  # Prevent caching of this view
def home(request):
    projects = Project.objects.all()  # Fetch all projects from the Griffin app
    context = {'projects': projects}
    return render(request, 'base/home.html', context)

# View function to handle login
def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')  # Use .get() to avoid KeyError
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect based on user type
            if user.is_staff:  # Check if the user is a staff member
                return redirect('dashboard_view')  # Redirect to the dashboard
            else:
                return redirect('home')  # Redirect to the home view for customers
        else:
            messages.error(request, 'Invalid username or password')  # Display error message
    return render(request, 'base/login.html')

# View function to handle signup
def signup_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists')
        else:
            user = User.objects.create_user(username=username, email=email, password=password)
            login(request, user)  # Automatically log in the user after signup
            return redirect('home')  # Redirect to home after signup

    return render(request, 'base/signup.html')  # Render the signup page

# View function for staff dashboard
@login_required(login_url='login')
@never_cache
def dashboard_view(request):
    # You can retrieve any relevant data for staff members here
    return render(request, 'griffin/dashboard.html')  # Render the dashboard template

# View function to handle logout
def logout_view(request):
    logout(request)
    return redirect('index')
