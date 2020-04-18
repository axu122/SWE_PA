from peer_assessment.models import User



def run():
	usr = User()
	tblname = usr._meta.db_table

	print(tblname)
	for u in User.objects.raw("SELECT * FROM peer_assessment_user"):
	# for u in User.objects.all():
		print(u)



# import os
# import sys
# sys.path.insert(0, "/DLL_Delivery4/peer_assessment")
	

# os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'DLL_Delivery4.DLL_Delivery4.settings') #maybe backslash?

# import django
# django.setup()


# from peer_assessment.models import User



# for u in User.objects.raw('SELECT * FROM DLL_Delivery4_Users'):
# 	print(u)
