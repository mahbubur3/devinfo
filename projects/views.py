from django.shortcuts import render, redirect

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
def create_project(request):
    form = ProjectForm()

    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('projects')
        
    context = {'form': form}
    return render(request, 'projects/create-project.html', context)


# edit project
def edit_project(request, pk):
    project = Project.objects.get(id=pk)
    form = ProjectForm(instance=project)

    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('projects')
        
    context = {'form': form}
    return render(request, 'projects/edit-project.html', context)


# delete a project
def delete_project(request, pk):
    project = Project.objects.get(id=pk)

    if request.method == 'POST':
        project.delete()
        return redirect('projects')
    
    context = {'project': project}
    return render(request, 'projects/delete-project.html', context)