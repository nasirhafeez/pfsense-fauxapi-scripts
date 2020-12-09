from usergroup_management import *
import pprint

UGMF = UserGroupManagementFauxapi(fauxapi_host, fauxapi_apikey, fauxapi_apisecret)

######################### OpenVPN User Setup #########################
#
# This script will create a static IP binding for OpenVPN user
# 
# It will be run with 3 command line arguments: username, static ip,
# subnet (in dotted decimal notation, like 255.255.255.0 for /24)
#
# python3 user_ovpn_setup.py username ip subnet
# 

user = UGMF.add_ovpn_csc(sys.argv[1], sys.argv[2], sys.argv[3])

pprint.pprint(user)