from django.views.decorators.csrf import csrf_exempt, requires_csrf_token
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from peer_assessment.models import *
# from snippets.models import Snippet
# from snippets.serializers import SnippetSerializer
import datetime
import json

#Gets the right assessments to be displayed on Professor assessment page
#Also handles csrf token in order to allow the request to go through
@requires_csrf_token
@api_view(['POST'])
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
    startDate = data.get("startDate")
    dueDate = data.get("dueDate")
    email = data.get("email")
    t = data.get("type")
    selectedClass = data.get("selectedClass")
    # selectedClass = json.loads(selectedClass)
    print(data)
    print(selectedClass)
    # -------------------------------------------
    b="F"
    c = Class.objects.get(pk=selectedClass)
    class_groups = Group.objects.filter(class_id=c)

    assessment = Assessment.objects.create(assessment_name=assessmentName, due_date=dueDate,
                                           start_date=startDate, class_id=c)
    assessment.save()
    qs = Question.objects.all()
    assess_qs = list()
    for q in qs:
        assess_q = Assessment_Question.objects.create(assessment_id=assessment, question_id=q)
        assess_q.save()
        assess_qs.append(assess_q)

    for group in class_groups:
        g_a= Group_Assessment.objects.create(group_id=group, assessment_id=assessment)
        g_a.save()
        group_students = Group_Student.objects.filter(group_id=group).values_list('student_id',flat=True)
        students = User.objects.filter(pk__in=group_students)
        print(students)
        for grader in students:
            for gradee in students:
                for aq in assess_qs:
                    grade = Grade.objects.create(grader=grader, gradee=gradee, assessment_question=aq)
                    grade.save()
    # print(assessment)
    #Try to write to database to add assessment to list, dummy code in place
    try:


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