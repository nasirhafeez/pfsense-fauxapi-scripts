#import subprocess
#subprocess.call("php /root/sg_reconfig.php")

import pprint, sys, os
from PfsenseFauxapi.PfsenseFauxapi import PfsenseFauxapi
from dotenv import load_dotenv

load_dotenv()

hostip = os.getenv("HOST_IP")
apikey = os.getenv("API_KEY")
apisecret = os.getenv("API_SECRET")

PfsenseFauxapi = PfsenseFauxapi(hostip, apikey, apisecret)

########## Script starts here ##########

stats = PfsenseFauxapi.function_call({
    'function': 'get_services',
})

pprint.pprint(stats)