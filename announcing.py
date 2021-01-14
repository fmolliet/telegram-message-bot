import sys
from Client import Automessager

Automessager().send_announce(str(sys.argv[1]))