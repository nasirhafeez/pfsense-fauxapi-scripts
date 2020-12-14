from usergroup_management import *
import pprint

UGMF = UserGroupManagementFauxapi(fauxapi_host, fauxapi_apikey, fauxapi_apisecret)

######################### SquidGuard Category Setup #########################
#
# This script will setup or modify a category in SquidGuard
# 
# It will be run without 1 command line argument: category
#
# python3 sg_add_category.py category
# 

user = UGMF.sg_add_category(sys.argv[1])

pprint.pprint(user)