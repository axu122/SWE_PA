from django.views.decorators.csrf import csrf_exempt, requires_csrf_token
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from peer_assessment.models import *
from django.http import JsonResponse
from django.core import serializers
# from snippets.models import Snippet
# from snippets.serializers import SnippetSerializer

#handles displaying contents on professor's homepage
#Also handles csrf token in order to allow the request to go through
@requires_csrf_token
@api_view(['POST'])
def view_professor_homepage(request):
    """
    List all code snippets, or create a new snippet.
    """
    print("In prof homepage servlet")
    data = request.data
    # print(data)
    email = data.get("email")
    t = data.get("type")
    # print(email, t)

    b="F"
    #Try to write to database to add assessment to list, dummy code in place

    try:
        professor = User.objects.get(email=email)
        classProfessors = Class_Professors.objects.filter(professor_id=professor)
        ids = list()
        for i in classProfessors:
            ids.append(i.class_id.id)
        classes = serializers.serialize('json', Class.objects.filter(pk__in=ids))
        print(classes)
        b="t"
    except:
        b = "F"
    print(b)
    # return JsonResponse(classes, safe=False, status=status.HTTP_200_OK)
    return Response(classes, status=status.HTTP_200_OK)

#handles displaying students homepage contents
#Also handles csrf token in order to allow the request to go through
@requires_csrf_token
@api_view(['POST'])
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