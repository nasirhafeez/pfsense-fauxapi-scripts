import pprint, sys, os
from PfsenseFauxapi.PfsenseFauxapi import PfsenseFauxapi
from dotenv import load_dotenv

load_dotenv()

hostip = os.getenv("HOST_IP")
apikey = os.getenv("API_KEY")
apisecret = os.getenv("API_SECRET")

########## Script starts here ##########

PfsenseFauxapi = PfsenseFauxapi(hostip, apikey, apisecret)
stats = PfsenseFauxapi.interface_stats('em0')
pprint.pprint(stats)