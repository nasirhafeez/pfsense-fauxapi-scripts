from usergroup_management import *
import pprint

UGMF = UserGroupManagementFauxapi(fauxapi_host, fauxapi_apikey, fauxapi_apisecret)

########################## OpenVPN Resync Script ##########################
#
# This script will resync OpenVPN users' static IP bindings
# 
# It will be run without any command line arguments:
#
# python3 user_ovpn_get.py
# 

users = UGMF.ovpn_resync()
pprint.pprint(users)