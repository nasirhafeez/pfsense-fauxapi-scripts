from usergroup_management import *
import pprint

UGMF = UserGroupManagementFauxapi(fauxapi_host, fauxapi_apikey, fauxapi_apisecret)

######################### User Delete Script #########################
# This script will delete an existing pfSense user
# 
# It will be run with 1 command line argument: username
#
# python3 user_delete.py username
# 
# In case the user does not exist it will produce an exception:
#               "user does not exist"
#

user = UGMF.remove_user(sys.argv[1])
pprint.pprint(user)