from usergroup_management import *
import pprint

UGMF = UserGroupManagementFauxapi(fauxapi_host, fauxapi_apikey, fauxapi_apisecret)

######################### SquidGuard Group ACL Removal Script #########################
#
# This script will delete a Group ACL in SquidGuard
# 
# It will be run with 1 command line argument: gacl_name
#
# python3 remove_sg_groupacl.py gacl_name
# 

user = UGMF.remove_sg_groupacl(sys.argv[1])

pprint.pprint(user)