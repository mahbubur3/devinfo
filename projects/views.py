from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Project, Tag
from .forms import ProjectForm, ReviewForm
from .utils import search_projects, paginate_projects


# show all projects and search
def projects(request):
    projects, search = search_projects(request)
    custom_range, projects = paginate_projects(request, projects, 9)

    context = {'projects': projects, 'search': search, 'custom_range': custom_range}
    return render(request, 'projects/projects.html', context)


# view project
def project(request, pk):
    project = Project.objects.get(id=pk)
    form = ReviewForm()

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        review = form.save(commit=False)
        review.project = project
        review.owner = request.user.profile
        review.save()

        project.vote_count

        messages.success(request, 'Your review was successfully submitted')
        return redirect('project', pk=project.id)

    context = {'project': project, 'form': form}
    return render(request, 'projects/project.html', context)


# create a project
@login_required(login_url='signin')
def create_project(request):
    profile = request.user.profile
    form = ProjectForm()

    if request.method == 'POST':
        new_tags = request.POST.get('newtags').replace(',', " ").split()
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.owner = profile
            project.save()

            for tag in new_tags:
                tag, created = Tag.objects.get_or_create(name=tag)
                project.tags.add(tag)
            return redirect('projects')
        
    context = {'form': form}
    return render(request, 'projects/project-form.html', context)


# edit project
@login_required(login_url='signin')
def edit_project(request, pk):
    profile = request.user.profile
    project = profile.project_set.get(id=pk)
    form = ProjectForm(instance=project)

    if request.method == 'POST':
        new_tags = request.POST.get('newtags').replace(',', " ").split()

        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            project = form.save()

            for tag in new_tags:
                tag, created = Tag.objects.get_or_create(name=tag)
                project.tags.add(tag)

            return redirect('account')
        
    context = {'form': form, 'project': project}
    return render(request, 'projects/project-form.html', context)


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