from usergroup_management import *
import pprint

UGMF = UserGroupManagementFauxapi(fauxapi_host, fauxapi_apikey, fauxapi_apisecret)

######################### SquidGuard Category Setup #########################
#
# This script will setup a category in SquidGuard
# 
# It will be run with 2 command line argument: category_name domain_list
#
# python3 sg_category_setup.py category "domain list e.g cnn.com github.com twitter.com"
# 

user = UGMF.add_sg_category(sys.argv[1], sys.argv[2])

pprint.pprint(user)