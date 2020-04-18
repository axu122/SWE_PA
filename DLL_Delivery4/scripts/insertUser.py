from peer_assessment.models import User
from django.db import connection

#Use insert to add dummy data into the db



def run():
    with connection.cursor() as cursor:
        #cursor.execute("INSERT INTO peer_assessment_user (first_name, last_name, email, password, eagle_id, type) VALUES ('Michael', 'Nam', 'namsg@bc.edu', '12345678', '82228375', 's')")
        #cursor.execute("Update peer_assessment_user set type = 'S' where first_name = 'Michael'") #updated type to capital S

        cursor.execute("select * from peer_assessment_user")
        row = cursor.fetchone() #fetches one data

        print(row)
        return row



	#cursor.execute("SELECT * FROM peer_assessment_user WHERE ~ = %s", variable)