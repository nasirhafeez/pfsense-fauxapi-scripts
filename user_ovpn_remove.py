from usergroup_management import *
import pprint

UGMF = UserGroupManagementFauxapi(fauxapi_host, fauxapi_apikey, fauxapi_apisecret)

######################### User Removal Script #########################
#
# This script will remove static IP binding of OpenVPN user. It is
# possible to have multiple entries for the same user in the OpenVPN
# Client Specific Overrides. This script just removes the first one
# amongst those entries.
# 
# It will be run with 1 command line argument: username
#
# python3 user_ovpn_remove.py username
# 

user = UGMF.remove_ovpn_csc(sys.argv[1])

pprint.pprint(user)