from usergroup_management import *
import pprint

UGMF = UserGroupManagementFauxapi(fauxapi_host, fauxapi_apikey, fauxapi_apisecret)

###################### User Get Script ######################
#
# This script will get and print the list of pfSense users
# 
# It will be run without any command line arguments:
#
# python3 user_get.py
# 

users = UGMF.get_users()
pprint.pprint(users)