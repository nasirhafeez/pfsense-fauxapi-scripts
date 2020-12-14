from usergroup_management import *
import pprint

UGMF = UserGroupManagementFauxapi(fauxapi_host, fauxapi_apikey, fauxapi_apisecret)

######################### SquidGuard Group ACL Setup #########################
#
# This script will setup or modify a Group ACL in SquidGuard
# 
# It will be run with 1 command line argument: group_acl_name
#
# python3 add_sg_groupacl.py group_acl_name
# 

user = UGMF.add_sg_groupacl(sys.argv[1])

pprint.pprint(user)