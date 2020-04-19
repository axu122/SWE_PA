from django.views.decorators.csrf import csrf_exempt, requires_csrf_token
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from peer_assessment.models import *
# from snippets.models import Snippet
# from snippets.serializers import SnippetSerializer

#handles displaying teams and students correctly
#Also handles csrf token in order to allow the request to go through
@requires_csrf_token
@api_view(['GET'])
def view_teams(request):
    """
    List all code snippets, or create a new snippet.
    """
    data = request.data
    email = data.get("email")
    t = data.get("type")
    print(data)
    print("In student homepage servlet")
    b="F"
    students = list()
    teams = list()
    try:
        professor = User.objects.get(email=email)
        #class = Class.objects.get(instructor_id = User.objects.get(email=email)
        #groups (which is a list) = Group.objejcts.get(class_id = class.class_id)
        #groupOnes = list()
            #for each group a in groups
                #groupOnes.append(Group_One.objects.get(group_id = a.group_id))
        #students = list()
        #for each groupOne b in groupOnes
            #students.append(User.objects.get(student_id = b.student_id))

        #These queries are to get all students from the class
        #write another query for class id where instructor_id = professor.id
        #write query on groups in the class based on matchinig class id
            #this will have gotten us all groups/team in the class

        # run through groupOne table to get all entries with groups from the class
        #query through user table where you match eagle id from group1 table to userid from usertable


        user = User.objects.get(email=email, password=currentPassword)
        b="t"
    except:
        b = "F"
    print(b)
    #data = list()
    #data.append(groups)
    #data.append(students)
    # return Response(data, status=status.HTTP_200_OK)
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