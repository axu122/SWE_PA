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
    # def default_pwd(self):
    #     s=""
    #     l = list()
    #     for i in range(8):
    #         l[i] = random.randint(0,9)
    #     return s.join(l)

    default_pwd = '12345678'

    first_name = models.CharField(max_length=100, null=False)
    last_name = models.CharField(max_length=100, null=False)
    email = models.EmailField(max_length=100, unique=True, null=False)
    password = models.CharField(
        max_length=100, null=False, default=default_pwd)
    eagle_id = models.CharField(verbose_name="id", max_length=8,
                                validators=[validate_digit_length], unique=True, null=False)
    type = models.CharField(max_length=1, choices=USER_TYPES, null=False)
