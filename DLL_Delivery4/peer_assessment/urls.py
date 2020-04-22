from django.urls import path

from . import views, requestHandler, changepassword, allassessmentsprof, homepages, teamshandler, studentpeerassessments
from rest_framework import routers
from .api import AssessmentViewSet

# router = routers.DefaultRouter()
# router.register('api/assessments', AssessmentViewSet, 'assessments')
# router.register('validate', )

# urlpatterns = router.urls

# app_name = 'peer_assessment'
#

#While most url navigation is handled by react, the one actual request made to validate uses this path so we can
# take the request and send it to the requestHandler server side
urlpatterns = [
    path('validate/', requestHandler.validate_user),
    path('verifychangepassword/', changepassword.change_password),
    path('addassessmentreq/', allassessmentsprof.add_assessment),
    path('assessmentview/', allassessmentsprof.view_assessments),
    # path('professorhomepage?<str:email>/<str:type>', homepages.view_professor_homepage),
    path('professorhomepage/', homepages.view_professor_homepage),
    path('studenthomepage/', homepages.view_student_homepage),
    path('studentteams/', teamshandler.view_teams),
    path('studentpeerassessments/', studentpeerassessments.view_assessments),
    path('studentcompletedassessments/', studentpeerassessments.view_completed_assessments),
    path('makenewteam/', teamshandler.add_team),
    path('makenewstudent/', teamshandler.add_student),
    path('professorgrade/', allassessmentsprof.professor_grade),
    path('studentgrade/', studentpeerassessments.student_grade)
]