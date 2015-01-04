from p2pool.bitcoin import networks

PARENT = networks.nets['unitus_blake']
SHARE_PERIOD = 15 			# seconds
CHAIN_LENGTH = 12*60*60//15 		# shares
REAL_CHAIN_LENGTH = 12*60*60//15 	# shares
TARGET_LOOKBEHIND = 10 			# shares
SPREAD = 30 				# blocks
IDENTIFIER = '3971a009b66f0805'.decode('hex')
PREFIX = '3971a009b66f0805'.decode('hex')
P2P_PORT = 51060
MIN_TARGET = 0
MAX_TARGET = 2**256//2**20 - 1
PERSIST = True
WORKER_PORT = 51050
BOOTSTRAP_ADDRS = 'nz.p2pool.geek.nz us.p2pool.geek.nz'.split(' ')
VERSION_CHECK = lambda v: True
