from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from .serializers import ProjectSerializer
from projects.models import Project, Review, Tag


@api_view(['GET'])
def get_projects(request):
    projects = Project.objects.all()
    serializer = ProjectSerializer(projects, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_project(request, pk):
    project = Project.objects.get(id=pk)
    serializer = ProjectSerializer(project, many=False)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def project_vote(request, pk):
    project = Project.objects.get(id=pk)
    user = request.user.profile
    data = request.data

    review, created = Review.objects.get_or_create(owner=user, project=project)

    review.value = data['value']
    review.save()
    project.vote_count

    serializer = ProjectSerializer(project, many=False)
    return Response(serializer.data)


@api_view(['DELETE'])
def remove_tag(request):
    tag_id = request.data['tag']
    project_id = request.data['project']

    project = Project.objects.get(id=project_id)
    tag = Tag.objects.get(id=tag_id)

    project.tags.remove(tag)

    return Response('Tag Deleted!')