from usergroup_management import *
import pprint

UGMF = UserGroupManagementFauxapi(fauxapi_host, fauxapi_apikey, fauxapi_apisecret)

######################### SquidGuard Category Update #########################
#
# This script will update an existing category in SquidGuard
# 
# It will be run with 2 command line argument: category_name domain_list
#
# python3 sg_category_setup.py category "updated domain list e.g cnn.com twitter.com"
# 

user = UGMF.update_sg_category(sys.argv[1], sys.argv[2])

pprint.pprint(user)