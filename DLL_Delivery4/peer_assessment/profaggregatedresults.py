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
        all_mc_questions = Question.objects.filter(type="Multiple Choice")
        questions = Assessment_Question.objects.filter(
            assessment_id=selectedAssessment)
        mc_questions = questions.filter(question_id__in=all_mc_questions)

        c = Class.objects.get(pk=selectedClass)
        g = Group.objects.filter(class_id=c)

        for team in g:
            stu = list()
            t = team.group_name

            gs = Group_Student.objects.filter(group_id=team)
            ids = list()
            for i in gs:
                ids.append(i.student_id.id)
            user_id = User.objects.filter(pk__in=ids)

            team_score_sum = 0
            team_member_count = 0
            for user in user_id:
                team_member_count += 1
                gradee = Grade.objects.filter(gradee=user)
                gradee = gradee.filter(assessment_question__in=mc_questions)
                score = 0
                count = 0
                for grad in gradee:
                    if(grad.score != ""):
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
                        "avg_score": avg_score
                    }
                )
            if team_member_count != 0:
                team_avg_score = team_score_sum/team_member_count
            else:
                team_avg_score = 0
            teamsGrid.append(
                {
                    "name": t,
                    "members": stu,
                    "avg_score": team_avg_score
                }
            )
        print(studentsGrid)
        print("@@@@@@@@@@@@@@")
        print(teamsGrid)
        b = "success"
    except:
        b = "Fail"
    print(b)

    return Response([studentsGrid, teamsGrid], status=status.HTTP_200_OK)
