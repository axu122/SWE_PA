from django.views.decorators.csrf import csrf_exempt, requires_csrf_token
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from peer_assessment.models import *
from peer_assessment.models import Assessment
# from snippets.models import Snippet
# from snippets.serializers import SnippetSerializer
import datetime

#Gets the right assessments to be displayed on Professor assessment page
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

#Code ran when the professor does add assessment
#Also handles csrf token in order to allow the request to go through
@requires_csrf_token
@api_view(['POST'])
def add_assessment(request):
    """
    List all code snippets, or create a new snippet.
    """
    data = request.data
    assessmentName = data.get("name")
    dueDate = data.get("dueDate")
    email = data.get("email")

    t = data.get("type")

    print(assessmentName)
    print(dueDate)

    b="F"

    #Try to write to database to add assessment to list, dummy code in place
    try:
        # assessment = Assessment.objects.create(assessment_name=assessmentName, due_date=dueDate, start_date=datetime.date, completion=False)
        # print(assessment)
        # assessment = Assignment.objects.create(assignment_name=assessmentName,
        #                                        due_date=dueDate,
        #                                        creation_date=datetime.date)
        b="t"
    except:
        b = "F"
    print(b)
    print(data)
    return Response(b, status=status.HTTP_200_OK)

#Code ran when the professor does grades assessment
#Also handles csrf token in order to allow the request to go through
@requires_csrf_token
@api_view(['POST'])
def professor_grade(request):
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