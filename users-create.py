from usergroup_management import *
import pprint

UGMF = UserGroupManagementFauxapi(fauxapi_host, fauxapi_apikey, fauxapi_apisecret)

# add_user
user = UGMF.add_user('test1')
#print(json.dumps(user))
pprint.pprint(user)

# manage_user attributes
attributes = {
    'disabled': False,
    'password': 'test123',
}
user = UGMF.manage_user('test1', attributes)
#print(json.dumps(user))
pprint.pprint(user)