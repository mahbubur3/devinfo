from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from .models import Project, Tag


# search project 
def search_projects(request):
    search = ''

    if request.GET.get('search'):
        search = request.GET.get('search')

    tags = Tag.objects.filter(name__icontains=search)

    projects = Project.objects.distinct().filter(
        Q(title__icontains=search) |
        Q(description__icontains=search) |
        Q(owner__name__icontains=search) |
        Q(tags__in=tags)
    )

    return projects, search


# paginate project 
def paginate_projects(request, projects, results):
    page = request.GET.get('page')
    results = 6
    paginator = Paginator(projects, results)

    try:
        projects = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        projects = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        projects = paginator.page(page)

    left_index = (int(page) - 4)

    if left_index < 1:
        left_index = 1

    right_index = (int(page) + 5)

    if right_index > paginator.num_pages:
        right_index = paginator.num_pages + 1

    custom_range = range(left_index, right_index)

    return custom_range, projects