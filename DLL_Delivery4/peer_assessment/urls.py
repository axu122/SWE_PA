from django.urls import path

from . import views, requestHandler, changepassword, addassessment, allassessmentsprof
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
    path('addassessmentreq/', addassessment.add_assessment),
    path('assessmentview/', allassessmentsprof.view_assessments)
]