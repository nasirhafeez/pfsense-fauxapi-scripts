import pprint, sys, os
from PfsenseFauxapi.PfsenseFauxapi import PfsenseFauxapi
from dotenv import load_dotenv
import usergroup-management

# load_dotenv()

# hostip = os.getenv("HOST_IP")
# apikey = os.getenv("API_KEY")
# apisecret = os.getenv("API_SECRET")

# PfsenseFauxapi = PfsenseFauxapi(hostip, apikey, apisecret)

########## Script starts here ##########

# config = PfsenseFauxapi.config_get()

# response_data = {}
# for user in config['system']['user']:
#     response_data[user['name']] = user
#     del(response_data[user['name']]['name'])
# pprint.pprint(response_data)

test = UserGroupManagementFauxapi.get_users()
pprint.pprint(test)