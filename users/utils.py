from django.db.models import Q

from .models import Profile, Skill


def search_profiles(request):
    search = ''

    if request.GET.get('search'):
        search = request.GET.get('search')

    skills = Skill.objects.filter(name__icontains=search)

    # search via name, intro and skill 
    profiles = Profile.objects.distinct().filter(
        Q(name__icontains=search) |
        Q(intro__icontains=search) |
        Q(skill__in=skills)
    )

    return profiles, search