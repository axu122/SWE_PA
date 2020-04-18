from django.views.decorators.csrf import csrf_exempt, requires_csrf_token
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from peer_assessment.models import *
# from snippets.models import Snippet
# from snippets.serializers import SnippetSerializer

#handles displaying students peer assessments
#Also handles csrf token in order to allow the request to go through
@requires_csrf_token
@api_view(['GET'])
def view_assessments(request):
    """
    List all code snippets, or create a new snippet.
    """
    data = request.data
    email = data.get("email")
    t = data.get("type")
    print(data)

    b="F"
    #Try to write to database to add assessment to list, dummy code in place
    try:
        # user = User.objects.get(email=email, password=currentPassword)
        b="t"
    except:
        b = "F"
    print(b)
    return Response(b, status=status.HTTP_200_OK)

#handles displaying students completed assessments
#Also handles csrf token in order to allow the request to go through
@requires_csrf_token
@api_view(['GET'])
def view_completed_assessments(request):
    """
    List all code snippets, or create a new snippet.
    """
    data = request.data
    email = data.get("email")
    t = data.get("type")
    print(data)

    b="F"
    #Try to write to database to add assessment to list, dummy code in place
    try:
        # user = User.objects.get(email=email, password=currentPassword)
        b="t"
    except:
        b = "F"
    print(b)
    return Response(b, status=status.HTTP_200_OK)

#Code ran when the student does assessment
#Also handles csrf token in order to allow the request to go through
@requires_csrf_token
@api_view(['POST'])
def student_grade(request):
    """
    List all code snippets, or create a new snippet.
    """
    data = request.data
    toDoIndex = data.get("toDoIndex")
    todoSelected = data.get("todoSelected")
    email = data.get("email")

    t = data.get("type")

    print(toDoIndex)
    print(todoSelected)

    b="F"
    #Try to write to database to add assessment to list, dummy code in place
    try:
        # user = User.objects.get(email=email, password=currentPassword)
        b="t"
    except:
        b = "F"
    print(b)
    print(data)
    return Response(b, status=status.HTTP_200_OK)