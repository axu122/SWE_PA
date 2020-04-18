from peer_assessment.models import User
from django.db import connection



def run():
    with connection.cursor() as cursor:

        cursor.execute("select * from peer_assessment_user")

        for row in cursor:
        	print(row)
        



	#cursor.execute("SELECT * FROM peer_assessment_user WHERE ~ = %s", variable)