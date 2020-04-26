from django.views.decorators.csrf import csrf_exempt, requires_csrf_token
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from peer_assessment.models import *
from django.core import serializers

# from snippets.models import Snippet
# from snippets.serializers import SnippetSerializer

# handles displaying students peer assessments
# Also handles csrf token in order to allow the request to go through
@requires_csrf_token
@api_view(['POST'])
def view_assessments(request):
    """
    List all code snippets, or create a new snippet.
    """
    print("view_assessments-student")
    data = request.data
    email = data.get("email")
    t = data.get("type")
    # selectedClass = data.get("selectedClass")
    selectedClass = 1

    b = "F"
    # Try to write to database to add assessment to list, dummy code in place
    try:
        student = User.objects.get(email=email)
        grader = Grade.objects.filter(grader=student)
        ids = list()
        for i in grader:
            ids.append(i.assessment_question.id)
        assess_q = Assessment_Question.objects.filter(pk__in=ids)

        ids2 = list()
        for i in assess_q:
            ids2.append(i.assessment_id.id)
        a = Assessment.objects.filter(pk__in=ids2)
        assessments = serializers.serialize('json', a)

        c = Class.objects.get(pk=selectedClass)

        assess_for_class = a.filter(class_id=c)
        assess_for_class_json = serializers.serialize('json', assess_for_class)
        print(assess_for_class_json)
        b = "t"
    except:
        b = "F"
    print(b)
    return Response(b, status=status.HTTP_200_OK)

# handles displaying students completed assessments
# Also handles csrf token in order to allow the request to go through
@requires_csrf_token
@api_view(['POST'])
def view_completed_assessments(request):
    """
    List all code snippets, or create a new snippet.
    """
    print("in view_completed_Assess")

    data = request.data
    email = data.get("email")
    t = data.get("type")
    print(data)
    selectedClass = 1

    b = "F"
    # Try to write to database to add assessment to list, dummy code in place
    try:
        student = User.objects.get(email=email)
        grader = Grade.objects.filter(grader=student)
        ids = list()
        for i in grader:
            ids.append(i.assessment_question.id)
        assess_q = Assessment_Question.objects.filter(pk__in=ids)

        ids2 = list()
        for i in assess_q:
            ids2.append(i.assessment_id.id)
        a = Assessment.objects.filter(pk__in=ids2)
        assessments = serializers.serialize('json', a)

        c = Class.objects.get(pk=selectedClass)

        assessment_for_specific_class = a.filter(class_id=c)
        completed = assessment_for_specific_class.filter(released=True)
        print(completed)
        completed_assessments = serializers.serialize('json', completed)
        print(completed_assessments)
        b = "t"
    except:
        b = "F"
    print(b)
    return Response(b, status=status.HTTP_200_OK)

# Code ran when the student does assessment
# Also handles csrf token in order to allow the request to go through
@requires_csrf_token
@api_view(['POST'])
def student_grade(request):
    """
    List all code snippets, or create a new snippet.
    """
    print("in student_grade")
    data = request.data
    toDoIndex = data.get("toDoIndex")
    todoSelected = data.get("todoSelected")
    email = data.get("email")

    t = data.get("type")

    print(toDoIndex)
    print(todoSelected)

    b = "F"
    # Try to write to database to add assessment to list, dummy code in place
    try:
        # user = User.objects.get(email=email, password=currentPassword)
        b = "t"
    except:
        b = "F"
    print(b)
    print(data)
    return Response(b, status=status.HTTP_200_OK)
