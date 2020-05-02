from django.views.decorators.csrf import csrf_exempt, requires_csrf_token
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from peer_assessment.models import *
from django.core import serializers
import datetime
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
    selectedClass = data.get("studentSelectedClass")

    b = "F"
    # Try to write to database to add assessment to list, dummy code in place
    # try:
    #get student
    student = User.objects.get(email=email)
    #get all grades where this student is the grader
    grader = Grade.objects.filter(grader=student)
    ids = list()
    #get all assessment questions in the grader
    for i in grader:
        ids.append(i.assessment_question.id)
    assess_q = Assessment_Question.objects.filter(pk__in=ids)

    ids2 = list()
    #get all assessments referenced in these assessment questions
    for i in assess_q:
        ids2.append(i.assessment_id.id)
    a = Assessment.objects.filter(pk__in=ids2)
    assessments = serializers.serialize('json', a)

    c = Class.objects.get(pk=selectedClass)
    group = Group.objects.filter(class_id=c)
    gs = Group_Student.objects.get(student_id=student, group_id__in=group)
    gS = Group_Student.objects.filter(group_id=gs.group_id)
    print(gS)
    ids3 = list()
    for i in gS:
        ids3.append(i.student_id.id)
    print(ids3)
    teamMembers = User.objects.filter(pk__in=ids3)
    print(teamMembers)
    members = list()
    for i in teamMembers:
        name = i.first_name + " " + i.last_name
        pk = i.id
        members.append(
            {
                "name": name,
                "pk": pk
            }
        )


    qpks = [x for x in range(1, 11)]
    qsMC = Question.objects.filter(pk__in=qpks, type='Multiple Choice')
    qsOR = Question.objects.filter(pk__in=qpks, type='Open Response')
    # print(qsMC)

    assess_for_class = a.filter(class_id=c)
    closed = list()
    open = list()
    for i in assess_for_class:
        if i.due_date > datetime.date.today():
            open.append(i)
        else:
            closed.append(i)
    openassessments = serializers.serialize('json', open)
    closedassessments = serializers.serialize('json', closed)
    g = serializers.serialize('json', group)
    # tM = serializers.serialize('json', members)
    questionsMC = serializers.serialize('json', qsMC)
    questionsOR = serializers.serialize('json', qsOR)

    b = "t"
    # except:
    #     b = "F"
    print(b)
    return Response([openassessments, closedassessments, members, questionsMC, questionsOR], status=status.HTTP_200_OK)


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
    selectedClass = data.get("studentSelectedClass")

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
    return Response(completed_assessments, status=status.HTTP_200_OK)

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
