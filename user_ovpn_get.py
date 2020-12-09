from usergroup_management import *
import pprint

UGMF = UserGroupManagementFauxapi(fauxapi_host, fauxapi_apikey, fauxapi_apisecret)

########################## OpenVPN User Get Script ##########################
#
# This script will get and print the list OpenVPN users' static IP bindings
# 
# It will be run without any command line arguments:
#
# python3 user_ovpn_get.py
# 

users = UGMF.get_ovpn_users()
pprint.pprint(users)