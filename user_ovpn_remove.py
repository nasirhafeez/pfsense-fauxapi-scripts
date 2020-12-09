from usergroup_management import *
import pprint

UGMF = UserGroupManagementFauxapi(fauxapi_host, fauxapi_apikey, fauxapi_apisecret)

######################### User Removal Script #########################
#
# This script will remove static IP binding of OpenVPN user
# 
# It will be run with 1 command line arguments: username
#
# python3 user_ovpn_remove.py username
# 

user = UGMF.remove_ovpn_csc('test')

pprint.pprint(user)