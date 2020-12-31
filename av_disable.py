from usergroup_management import *
import pprint

UGMF = UserGroupManagementFauxapi(fauxapi_host, fauxapi_apikey, fauxapi_apisecret)

######################### Disable ClamAV Anti-Virus #########################
#
# This script will disable ClamAV anti-virus feature in Squid
# 
# It will be run with no command line arguments
#
# python3 av_disable.py
# 

#step1 = UGMF.disable_av()
step2 = UGMF.delete_av_cron()

#pprint.pprint(step1)
pprint.pprint(step2)