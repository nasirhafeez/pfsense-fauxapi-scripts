import pprint, sys, os

sys.path.append(".")

from usergroup_management import *

UGMF = UserGroupManagementFauxapi(fauxapi_host, fauxapi_apikey, fauxapi_apisecret)
users = UGMF.get_users()
pprint.pprint(users)