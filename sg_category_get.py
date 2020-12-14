from usergroup_management import *
import pprint

UGMF = UserGroupManagementFauxapi(fauxapi_host, fauxapi_apikey, fauxapi_apisecret)

######################### SquidGuard Category Get Setup #########################
#
# This script will get and print the list of categories in SquidGuard
# 
# It will be run without any command line arguments:
#
# python3 get_sg_category.py
# 

user = UGMF.get_sg_category()

pprint.pprint(user)