from django.views.decorators.csrf import csrf_exempt, requires_csrf_token
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from peer_assessment.models import *
from django.core import serializers

# from snippets.models import Snippet
# from snippets.serializers import SnippetSerializer
import datetime
import json


@requires_csrf_token
@api_view(['POST'])
def view_aggregated_results(request):
    """
    List all code snippets, or create a new snippet.
    """
    data = request.data
    email = data.get("email")
    t = data.get("type")
    selectedClass = data.get("selectedClass")
    selectedAssessment = data.get("selectedAssessment")
    print(data)

    print("In student homepage servlet")
    b = "Fail"

    # students = list()
    # teams = list()
    studentsGrid = list()
    teamsGrid = list()
    try:

        c = Class.objects.get(pk=selectedClass)
        g = Group.objects.filter(class_id=c)
        # groups = serializers.serialize('json', g)

        # gs = Group_Student.objects.filter(group_id__in=g).values_list("student_id", flat=True)
        # s = User.objects.filter(pk__in=gs)
        # students = serializers.serialize('json', s)  # converts query set into json string.
        # print(groups)
        # print(students)

        for team in g:
            print("made it in the loop")
            gs = Group_Student.objects.filter(group_id=team).values_list("student_id", flat=True)
            print("made it past query 1")
            s = User.objects.filter(pk__in=gs).values_list('first_name', 'last_name')
            stu = list()
            # print(s)
            t = team.group_name
            for student in s:
                name = student[0] + " " + student[1]
                stu.append(name)
                print("made to end of second loop")
                studentsGrid.append(
                    {
                        "name": name,
                        "team": t
                    }
                )
            teamsGrid.append(
                {
                    "name": t,
                    "members": stu
                }
            )
        print(studentsGrid)
        print(teamsGrid)

        b = "success"
    except:
        b = "Fail"

    print(b)

    # return Response([groups, students], status=status.HTTP_200_OK)
    return Response([studentsGrid, teamsGrid], status=status.HTTP_200_OK)