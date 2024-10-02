# griffin/views.py
from django.shortcuts import render, redirect
from .models import Project
from .forms import ProjectForm
from django.views.decorators.cache import never_cache  # Import never_cache

# View function to handle project creation
def create_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirect to the Base home view after saving
    else:
        form = ProjectForm()
    return render(request, 'griffin/create_project.html', {'form': form})

# View function to list all projects
def list_projects(request):
    projects = Project.objects.all()  # Fetch all projects from the Griffin app
    return render(request, 'griffin/list_projects.html', {'projects': projects})

# View function for staff dashboard
@never_cache  # Prevent caching of this view
def dashboard_view(request):
    projects = Project.objects.all()  # Fetch all projects for display in the dashboard
    return render(request, 'griffin/dashboard.html', {'projects': projects})



