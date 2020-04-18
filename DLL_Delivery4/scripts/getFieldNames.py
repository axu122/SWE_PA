from peer_assessment.models import User
from django.db import connection



def run():
	sql = "select * from peer_assessment_user"
	cursor = connection.cursor()
	cursor.execute(sql)
	rows = cursor.description
	print(rows)
