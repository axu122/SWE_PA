from peer_assessment.models import User
from django.db import connection



def run():
	with connection.cursor() as cursor:
    	cursor.execute("INSERT INTO peer_assessment_user (first_name, last_name, email, password, eagle_id, type) VALUES ('Michael', 'Nam', 'namsg@bc.edu', '12345678', '82228375', 's')")
        cursor.execute("select * from peer_assessment_user")
        row = cursor.fetchone()

    	print(row)
    	return row



	#cursor.execute("SELECT * FROM peer_assessment_user WHERE ~ = %s", variable)