from usergroup_management import *
import pprint

UGMF = UserGroupManagementFauxapi(fauxapi_host, fauxapi_apikey, fauxapi_apisecret)

user = UGMF.remove_user(sys.argv[1])

pprint.pprint(user)