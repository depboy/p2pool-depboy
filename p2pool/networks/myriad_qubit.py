from p2pool.bitcoin import networks

PARENT = networks.nets['myriad_qubit']
SHARE_PERIOD = 10 # seconds
CHAIN_LENGTH = 24*60*60//10 # shares
REAL_CHAIN_LENGTH = 24*60*60//10 # shares
TARGET_LOOKBEHIND = 50 # shares
SPREAD = 30 # blocks
IDENTIFIER = 'fc70135c700a00ee'.decode('hex')
PREFIX = '9472ef181e88efcb'.decode('hex')
P2P_PORT = 5566
MIN_TARGET = 0
MAX_TARGET = 2**256//2**20 - 1
PERSIST = True
WORKER_PORT = 5567
BOOTSTRAP_ADDRS = 'p2poolcoin.com'.split(' ')
VERSION_CHECK = lambda v: True
