#import subprocess
#subprocess.call("php /root/sg_reconfig.php")

import pprint, sys
from PfsenseFauxapi.PfsenseFauxapi import PfsenseFauxapi
PfsenseFauxapi = PfsenseFauxapi('192.168.100.54', 'PFFAudv9Chfn2n7W1us5utjH', '9XjKvnBRdNDCviXr9bZsTzKkIl4rZwp06gs0ImW4vV6kE1k16ibJ4SyPLJcz')

stats = PfsenseFauxapi.interface_stats('em0')
pprint.pprint(stats) 