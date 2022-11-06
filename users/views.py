from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
 
from .forms import CustomUserCreationForm, ProfileForm, SkillForm
from .models import Profile, Message
from .utils import search_profiles, paginate_profiles


# user login 
def signin(request):
    page = 'signin'

    # if user is authenticated then not redirect to signin page
    if request.user.is_authenticated:
        return redirect('profiles')

    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'Username does not exist')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect(request.GET['next'] if 'next' in request.GET else 'account')
        else:
            messages.error(request, 'Username or Password is incorrect')

    return render(request, 'users/signin-signup.html')


# user logout
def signout(request):
    logout(request)
    messages.info(request, 'User was successfully logged out')
    return redirect('signin')


# user registration
def signup(request):
    page = 'signup'
    form = CustomUserCreationForm()

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request, 'User account was created successfully')

            # when registration is done then automatically login and redirect to profiles 
            login(request, user)
            return redirect('account')
        
        else:
            messages.error(request, 'An error has occurred during signup')

    context = {'page': page, 'form': form}
    return render(request, 'users/signin-signup.html', context)


# show all profiles
def profiles(request):
    profiles, search = search_profiles(request)
    custom_range, profiles = paginate_profiles(request, profiles, 9)

    context = {'profiles': profiles, 'search': search, 'custom_range': custom_range}
    return render(request, 'users/profiles.html', context)


# show user profile
def profile(request, pk):
    profile = Profile.objects.get(id=pk)

    # show skills 
    top_skills = profile.skill_set.exclude(description__exact="")
    other_skills = profile.skill_set.filter(description="")

    context = {'profile': profile, 'top_skills': top_skills, 'other_skills': other_skills}
    return render(request, 'users/profile.html', context)


# user account 
@login_required(login_url='signin')
def user_account(request):
    profile = request.user.profile

    skills = profile.skill_set.all()
    projects = profile.project_set.all()

    context = {'profile': profile, 'skills': skills, 'projects': projects}
    return render(request, 'users/user-account.html', context)


# edit user account 
@login_required(login_url='signin')
def edit_account(request):
    profile = request.user.profile
    form = ProfileForm(instance=profile)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('account')

    context = {'form': form}
    return render(request, 'users/profile-form.html', context)


# add user skill
@login_required(login_url='signin')
def add_skill(request):
    profile = request.user.profile
    form = SkillForm()

    if request.method == 'POST':
        form = SkillForm(request.POST)
        if form.is_valid():
            skill = form.save(commit=False)
            skill.owner = profile
            skill.save()
            messages.success(request, 'Skill was added successfully')
            return redirect('account')

    context = {'form': form}
    return render(request, 'users/skill-form.html', context)


# add user skill
@login_required(login_url='signin')
def edit_skill(request, pk):
    profile = request.user.profile
    skill = profile.skill_set.get(id=pk)
    form = SkillForm(instance=skill)

    if request.method == 'POST':
        form = SkillForm(request.POST,instance=skill)
        if form.is_valid():
            form.save()
            messages.success(request, 'Skill was updated successfully')
            return redirect('account')

    context = {'form': form}
    return render(request, 'users/skill-form.html', context)


def delete_skill(request, pk):
    profile = request.user.profile
    skill = profile.skill_set.get(id=pk)

    if request.method == 'POST':
        skill.delete()
        messages.success(request, 'Skill was deleted successfully')
        return redirect('account')

    context = {'object': skill}
    return render(request, 'delete-template.html', context)


# messages
@login_required(login_url='signin')
def inbox(request):
    profile = request.user.profile
    message_requests = profile.messages.all()
    unread_count = message_requests.filter(is_read=False).count()

    context = {'message_requests': message_requests, 'unread_count': unread_count}
    return render(request, 'users/inbox.html', context)


@login_required(login_url='signin')
def view_message(request, pk):
    profile = request.user.profile
    message = profile.messages.get(id=pk)

    if message.is_read == False:
        message.is_read = True
        message.save()

    context = {'message': message}
    return render(request, 'users/message.html', context)