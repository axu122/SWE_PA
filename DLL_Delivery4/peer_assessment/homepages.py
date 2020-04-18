from django.views.decorators.csrf import csrf_exempt, requires_csrf_token
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from peer_assessment.models import *
# from snippets.models import Snippet
# from snippets.serializers import SnippetSerializer

#Also handles csrf token in order to allow the request to go through
@requires_csrf_token
@api_view(['GET'])
def view_professor_homepage(request):
    """
    List all code snippets, or create a new snippet.
    """

    data = request.data
    email = data.get("email")
    t = data.get("type")
    print(data)
    print("In prof homepage servlet")
    b="F"
    #Try to write to database to add assessment to list, dummy code in place
    try:
        # user = User.objects.get(email=email, password=currentPassword)
        b="t"
    except:
        b = "F"
    print(b)
    return Response(b, status=status.HTTP_200_OK)


#Also handles csrf token in order to allow the request to go through
@requires_csrf_token
@api_view(['GET'])
def view_student_homepage(request):
    """
    List all code snippets, or create a new snippet.
    """
    data = request.data
    email = data.get("email")
    t = data.get("type")
    print(data)
    print("In student homepage servlet")
    b="F"
    #Try to write to database to add assessment to list, dummy code in place
    try:
        # user = User.objects.get(email=email, password=currentPassword)
        b="t"
    except:
        b = "F"
    print(b)
    return Response(b, status=status.HTTP_200_OK)