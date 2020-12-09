from usergroup_management import *
import pprint

UGMF = UserGroupManagementFauxapi(fauxapi_host, fauxapi_apikey, fauxapi_apisecret)

# add_user
user = UGMF.add_user(sys.argv[1])
#print(json.dumps(user))
pprint.pprint(user)

# manage_user attributes
attributes = {
    'disabled': False,
    'password': sys.argv[2],
}
user = UGMF.manage_user(sys.argv[1], attributes)
#print(json.dumps(user))
pprint.pprint(user)