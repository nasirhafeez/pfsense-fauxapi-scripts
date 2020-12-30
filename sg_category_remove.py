from usergroup_management import *
import pprint

UGMF = UserGroupManagementFauxapi(fauxapi_host, fauxapi_apikey, fauxapi_apisecret)

######################### SquidGuard Category Removal Script #########################
#
# This script will delete a category in SquidGuard
# 
# It will be run with 1 command line argument: category
#
# python3 sg_category_remove.py category
# 

user = UGMF.remove_sg_category(sys.argv[1])

pprint.pprint(user)