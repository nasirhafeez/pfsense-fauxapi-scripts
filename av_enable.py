from usergroup_management import *
import pprint

UGMF = UserGroupManagementFauxapi(fauxapi_host, fauxapi_apikey, fauxapi_apisecret)

######################### Enable ClamAV Anti-Virus #########################
#
# This script will enable ClamAV anti-virus feature in Squid
# 
# It will be run with no command line arguments
#
# python3 av_enable.py
# 

user = UGMF.enable_av()

pprint.pprint(user)