from django.contrib import admin
from .models import User, GroupOne, Group, AssignmentOne, Assignment, Question, QuestionOne, Class, Eval_set, GraderOne, Grader
# Register your models here.
admin.site.register(User)
admin.site.register(GroupOne)
admin.site.register(Group)
admin.site.register(AssignmentOne)
admin.site.register(Assignment)
admin.site.register(Question)
admin.site.register(QuestionOne)
admin.site.register(Class)
admin.site.register(Eval_set)
admin.site.register(GraderOne)
admin.site.register(Grader)
