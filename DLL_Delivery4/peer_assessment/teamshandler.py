from django.views.decorators.csrf import csrf_exempt, requires_csrf_token
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from peer_assessment.models import *
from django.core import serializers
# from snippets.models import Snippet
# from snippets.serializers import SnippetSerializer

#handles displaying teams and students correctly
#Also handles csrf token in order to allow the request to go through
#COMPLETE?? 
@requires_csrf_token
@api_view(['POST'])
def view_teams(request):
    """
    List all code snippets, or create a new snippet.
    """
    data = request.data
    email = data.get("email")
    t = data.get("type")
    selectedClass = data.get("selectedClass")

    print(data)

    print("In student homepage servlet")
    b="Fail"

    try:
        students = list()
        teams = list()
        c = Class.objects.get(pk=selectedClass)
        g = Group.objects.filter(class_id = c)
        groups = serializers.serialize('json', g)
        gs = Group_Student.objects.filter(group_id__in = g).values_list("student_id", flat=True)
        s = User.objects.filter(pk__in = gs)
        students = serializers.serialize('json', s) #converts query set into json string. 
        
        print(groups)
        print()
        print(students)
       
        b="success"
    except:
        b = "Fail"

    print(b)


    return Response(b, status=status.HTTP_200_OK)

#handles add team button functionality
#Also handles csrf token in order to allow the request to go through
@requires_csrf_token
@api_view(['POST'])
def add_team(request):
    """
    List all code snippets, or create a new snippet.
    """
    data = request.data
    name = data.get("name")
    members = data.get("members")
    overallGrade = data.get("overallGrade")
    email = data.get("email")

    t = data.get("type")

    b="F"
    #Try to write to database to add assessment to list, dummy code in place
    try:
        # group = Group.objects.add(fill out stuff you need to add) Look up code for inserting into table
        # group.save()

        b="t"
    except:
        b = "F"
    print(b)
    print(data)
    return Response(b, status=status.HTTP_200_OK)

#handles add student button functionality
#Also handles csrf token in order to allow the request to go through
@requires_csrf_token
@api_view(['POST'])
def add_student(request):
    """
    List all code snippets, or create a new snippet.
    """
    data = request.data
    name = data.get("name")
    team = data.get("team")
    overallGrade = data.get("overallGrade")
    email = data.get("email")

    t = data.get("type")

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