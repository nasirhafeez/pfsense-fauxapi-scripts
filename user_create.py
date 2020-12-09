from usergroup_management import *
import pprint

UGMF = UserGroupManagementFauxapi(fauxapi_host, fauxapi_apikey, fauxapi_apisecret)

######################### User Create Script #########################
#
# This script will create a new pfSense user
# 
# It will be run with 2 command line arguments: username, password
#
# python3 user_create.py username password
# 

# add_user
user = UGMF.add_user(sys.argv[1])

# manage_user attributes (assign password)
attributes = {
    'disabled': False,
    'password': sys.argv[2],
}
user = UGMF.manage_user(sys.argv[1], attributes)

pprint.pprint(user)