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

    b = "Fail"

    studentsGrid = list()
    teamsGrid = list()

    try:
        # qpks = [x for x in range(1, 11)]
        all_mc_questions = Question.objects.filter(type="Multiple Choice")
        mc_questions = Assessment_Question.objects.filter(
            assessment_id=selectedAssessment, question_id__in=all_mc_questions)

        # Get CLASS and GROUPS
        c = Class.objects.get(pk=selectedClass)
        g = Group.objects.filter(class_id=c)
        print(g)
        for team in g:
            stu = list()
            t = team.group_name
            print(t)
            gs = Group_Student.objects.filter(group_id=team)
            ids = list()
            for i in gs:
                ids.append(i.student_id.id)

            # Have STUDENTS in TEAM
            user_id = User.objects.filter(pk__in=ids)
            print(user_id)
            team_score_sum = 0
            team_member_count = 0
            for user in user_id:
                team_member_count += 1
                gradee = Grade.objects.filter(gradee=user, assessment_question__in=mc_questions)
                grader = Grade.objects.filter(grader=user, assessment_question__in=mc_questions,completion=False)
                print("len(grader)=" +str(len(grader)))

                score = 0
                count = 0
                avg_score = 0
                # If it is not then we do nothing right now, but we could make all the other grades
                # of this student in the db 0. Right now, we just do math to make it 0
                if(len(grader)==0):
                    for grad in gradee:
                        # If score isn't filled out the value of it is NONE

                        if(grad.assessment_question.question_id.type=='Multiple Choice' and grad.completion==True):
                            score += int(grad.score)
                        count += 1
                    avg_score = score/count
                team_score_sum += avg_score
                name = user.first_name + " " + user.last_name

                stu.append(name)

                studentsGrid.append(
                    {
                        "name": name,
                        "team": t,
                        "avg_score": round(avg_score,2)
                    }
                )
            print(studentsGrid)
            if team_member_count != 0:
                team_avg_score = team_score_sum/team_member_count
            else:
                team_avg_score = 0
            teamsGrid.append(
                {
                    "name": t,
                    "members": stu,
                    "avg_score": round(team_avg_score,2)
                }
            )
            print(teamsGrid)
        print(studentsGrid)
        print("@@@@@@@@@@@@@@")
        print(teamsGrid)
        b = "success"
    except:
        b = "Fail"
    print(b)

    return Response([studentsGrid, teamsGrid], status=status.HTTP_200_OK)


@requires_csrf_token
@api_view(['POST'])
def release_results(request):
    """
        List all code snippets, or create a new snippet.
        """
    data = request.data
    email = data.get("email")
    t = data.get("type")
    # selectedClass = data.get("selectedClass")
    selectedAssessment = data.get("selectedAssessment")
    a = Assessment.objects.get(pk=selectedAssessment)
    print(a)
    a.released = True
    a.save()
    b = "Fail"
    try:

        b = "success"
    except:
        b = "Fail"
    print(b)
    return Response(b, status=status.HTTP_200_OK)

@requires_csrf_token
@api_view(['POST'])
def download_results(request):
    """
        List all code snippets, or create a new snippet.
        """
    data = request.data
    email = data.get("email")
    t = data.get("type")
    # selectedClass = data.get("selectedClass")
    # selectedAssessment = data.get("selectedAssessment")

    b = "Fail"
    try:

        b = "success"
    except:
        b = "Fail"
    print(b)
    return Response(b, status=status.HTTP_200_OK)

