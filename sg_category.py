from usergroup_management import *
import pprint

UGMF = UserGroupManagementFauxapi(fauxapi_host, fauxapi_apikey, fauxapi_apisecret)

######################### SquidGuard Category Setup #########################
#
# This script setup or modify a category in SquidGuard
# 
# It will be run without any command line arguments:
#
# python3 sg_category.py
# 

user = UGMF.sg_category(sys.argv[1])

pprint.pprint(user)