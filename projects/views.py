from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Project, Tag
from .forms import ProjectForm
from .utils import search_projects, paginate_projects


# show all projects and search
def projects(request):
    projects, search = search_projects(request)
    custom_range, projects = paginate_projects(request, projects, 6)

    context = {'projects': projects, 'search': search, 'custom_range': custom_range}
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
            return redirect('account')
        
    context = {'form': form}
    return render(request, 'projects/edit-project.html', context)


# delete a project
@login_required(login_url='signin')
def delete_project(request, pk):
    profile = request.user.profile
    project = profile.project_set.get(id=pk)

    if request.method == 'POST':
        project.delete()
        messages.success(request, 'Project was deleted successfully')
        return redirect('account')
    
    context = {'object': project}
    return render(request, 'delete-template.html', context)