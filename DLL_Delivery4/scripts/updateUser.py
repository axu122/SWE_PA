from peer_assessment.models import User
from django.db import connection



def run():
	with connection.cursor() as cursor:
    	cursor.execute("UPDATE bar SET foo = 1 WHERE baz = %s", [self.baz])
        cursor.execute("SELECT foo FROM bar WHERE baz = %s", [self.baz])
        row = cursor.fetchone()

    print(row)
    return row


	sql = "select * from peer_assessment_user"
	cursor = connection.cursor()
	cursor.execute(sql)

	for u in User.objects.raw("SELECT * FROM peer_assessment_user"):
		print(u)