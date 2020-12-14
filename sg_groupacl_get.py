from usergroup_management import *
import pprint

UGMF = UserGroupManagementFauxapi(fauxapi_host, fauxapi_apikey, fauxapi_apisecret)

######################### SquidGuard Group ACL Get Script #########################
#
# This script will get and print the list of Group ACLs in SquidGuard
# 
# It will be run without any command line arguments:
#
# python3 get_sg_groupacl.py
# 

user = UGMF.get_sg_groupacl()

pprint.pprint(user)