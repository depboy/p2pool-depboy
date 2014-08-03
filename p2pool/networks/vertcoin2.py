from p2pool.bitcoin import networks

PARENT = networks.nets['vertcoin']
SHARE_PERIOD = 15 # seconds
CHAIN_LENGTH = 24*60*60//10 # shares
REAL_CHAIN_LENGTH = 24*60*60//10 # shares
TARGET_LOOKBEHIND = 200 # shares
SPREAD = 12 # blocks
IDENTIFIER = 'a06a81c827cab974'.decode('hex')
PREFIX = '7c3614a6bcdcf795'.decode('hex')
P2P_PORT = 9347
MIN_TARGET = 4
MAX_TARGET = 2**256//2**20 - 1
PERSIST = True
WORKER_PORT = 9172
BOOTSTRAP_ADDRS = 'lovok.no-ip.com us-east.p2pools.net us-central.p2pools.net us-west.p2pools.net vert.marcsi.ch'.split(' ')
ANNOUNCE_CHANNEL='#p2pool-vtc'
VERSION_CHECK = lambda v: True
