from usergroup_management import *
import pprint

UGMF = UserGroupManagementFauxapi(fauxapi_host, fauxapi_apikey, fauxapi_apisecret)

######################### User Create Script #########################
# This script will create a new pfSense user
# 
# It will be run with 2 command line arguments: username, password
#
# python3 user_create.py username password
# 

# add_user
user = UGMF.add_ovpn_csc('test5')

pprint.pprint(user)