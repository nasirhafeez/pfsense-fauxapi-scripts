from usergroup_management import *
import pprint

UGMF = UserGroupManagementFauxapi(fauxapi_host, fauxapi_apikey, fauxapi_apisecret)

######################### SquidGuard Category Setup #########################
#
# This script will setup or modify a category in SquidGuard
# 
# It will be run with 1 command line argument: category domain_list
#
# python3 add_sg_category.py category "domain list"
# 

user = UGMF.add_sg_category(sys.argv[1], sys.argv[2])

pprint.pprint(user)