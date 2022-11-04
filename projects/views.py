from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import Project
from .forms import ProjectForm


# show all projects in homepage
def projects(request):
    projects = Project.objects.all()

    context = {'projects': projects}
    return render(request, 'projects/projects.html', context)


# view project
def project(request, pk):
    project = Project.objects.get(id=pk)

    context = {'project': project}
    return render(request, 'projects/project.html', context)


# create a project
@login_required(login_url='signin')
def create_project(request):
    profile = request.user.profile
    form = ProjectForm()

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.owner = profile
            project.save()
            return redirect('projects')
        
    context = {'form': form}
    return render(request, 'projects/create-project.html', context)


# edit project
@login_required(login_url='signin')
def edit_project(request, pk):
    profile = request.user.profile
    project = profile.project_set.get(id=pk)
    form = ProjectForm(instance=project)

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect('projects')
        
    context = {'form': form}
    return render(request, 'projects/edit-project.html', context)


# delete a project
@login_required(login_url='signin')
def delete_project(request, pk):
    profile = request.user.profile
    project = profile.project_set.get(id=pk)

    if request.method == 'POST':
        project.delete()
        return redirect('projects')
    
    context = {'project': project}
    return render(request, 'projects/delete-project.html', context)