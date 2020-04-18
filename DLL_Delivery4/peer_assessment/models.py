import datetime
import random
from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone

# Create your models here.
# User model is the model for users based on name, email, id, pwd, and type of user.


class User(models.Model):
    def __str__(self):
        return self.email
    USER_TYPES = [
        ('S', 'Student'),
        ('I', 'Instructor'),
        ('T', 'TA'),
        ('A', 'Administrator')
    ]

    def validate_digit_length(eagle_id):
        if not (eagle_id.isdigit() and len(eagle_id) == 8):
            raise ValidationError('%(id)s must be 8 digits',
                                  params={'id': eagle_id}, )
    def default_pwd():
        r = random.randint(11111111,99999999)
        return str(r)

    first_name = models.CharField(max_length=100, null=False)
    last_name = models.CharField(max_length=100, null=False)
    email = models.EmailField(max_length=100, unique=True, null=False)
    password = models.CharField(
        max_length=100, null=False, default= default_pwd())
    eagle_id = models.CharField(verbose_name="id", max_length=8, validators=[validate_digit_length],
                                unique=True, null=False, primary_key=True)
    type = models.CharField(max_length=1, choices=USER_TYPES, null=False)


class Question(models.Model):
    def __str__(self):
        return self.question

    question_id = models.CharField(max_length=100, primary_key=True)
    question = models.CharField(max_length=100, null=False)
    grade = models.CharField(max_length=100, null=False)


class Group(models.Model):
    def __str__(self):
        return self.group_name
    group_id = models.CharField(max_length=100, primary_key=True)
    num_students = models.CharField(max_length=100, unique=False, null=False)
    group_name = models.CharField(max_length=100, unique=True, null=False)


class GroupOne(models.Model):
    def validate_digit_length(eagle_id):
        if not (eagle_id.isdigit() and len(eagle_id) == 8):
            raise ValidationError('%(id)s must be 8 digits',
                                  params={'id': eagle_id}, )

    eagle_id = models.ForeignKey(User, on_delete=models.CASCADE)
    group_id = models.ForeignKey(Group, on_delete=models.CASCADE)
    key_1 = models.CharField(max_length=100, primary_key=True)


class Class(models.Model):
    def __str__(self):
        return self.class_name

    class_id = models.CharField(max_length=100, primary_key=True)
    professor_name = models.CharField(max_length=100, null=False)
    class_name = models.CharField(max_length=100, null=False)
    section = models.CharField(max_length=100, null=False)
    semester = models.CharField(max_length=100, null=False)
    code = models.CharField(max_length=100, null=False)
    instructor_list_id = models.CharField(max_length=100, null=False)



class Assignment(models.Model):
    def __str__(self):
        return self.assignment_name

    assignment_id = models.CharField(max_length=100, primary_key=100)

    assignment_name = models.CharField(max_length=100)
    creation_date = models.DateField(auto_now=True)
    due_date = models.DateField()
    completion = models.BooleanField()
    qset_id = models.CharField(max_length=100, null=False)

    class_id = models.ForeignKey(Class, on_delete=models.CASCADE)


class Eval_set(models.Model):
    def __str__(self):
        return self.student_name + " " + self.eval_set_id
    eval_set_id = models.CharField(max_length=100, null=False, primary_key=True)
    student_name = models.CharField(max_length=100, null=False)
    student_name = models.CharField(max_length=100, null=False)
    student_name = models.CharField(max_length=100, null=False)

class Grader(models.Model):

    assignment_id = models.ForeignKey(Assignment, on_delete=models.CASCADE)
    eval_set_id = models.ForeignKey(Eval_set, on_delete=models.CASCADE)
    grader_name = models.CharField(max_length=100, null=False)
    grader_ass_id = models.CharField(max_length=100, primary_key=True)
    aggregate_score = models.CharField(max_length=100, null=False)


class AssignmentOne(models.Model):
    group_id = models.ForeignKey(Group, on_delete=models.CASCADE)
    assignment_id = models.ForeignKey(Assignment, on_delete=models.CASCADE)

    key_2 = models.CharField(max_length=100, primary_key=True)


class QuestionOne(models.Model):
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE)
    qset_id = models.ForeignKey(Assignment, on_delete=models.CASCADE)

    key_3 = models.CharField(max_length=100, primary_key=True)


class GraderOne(models.Model):
    grader_id = models.ForeignKey(User, on_delete=models.CASCADE)
    grader_ass_id = models.OneToOneField(Grader,on_delete=models.CASCADE)

class Instructors(models.Model):
    instructor_id = models.OneToOneField(User,on_delete=models.CASCADE)

class InstructorSet(models.Model):
    instructor_list_id = models.ForeignKey(Class, on_delete=models.CASCADE)
    instructor_id = models.OneToOneField(Instructors,on_delete=models.CASCADE)
    key_id = models.CharField(max_length=100, primary_key=True)