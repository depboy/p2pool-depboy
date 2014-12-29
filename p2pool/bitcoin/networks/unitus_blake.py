import os
import platform

from twisted.internet import defer

from .. import data, helper
from p2pool.util import pack


P2P_PREFIX = 'c5abc69d'.decode('hex')
P2P_PORT = 50603
ADDRESS_VERSION = 68
RPC_PORT = 50604
RPC_CHECK = defer.inlineCallbacks(lambda bitcoind: defer.returnValue(
            'unitusaddress' in (yield bitcoind.rpc_help()) and
            not (yield bitcoind.rpc_getinfo())['testnet']
        ))
SUBSIDY_FUNC = lambda height: 100000000 * 100 * math.pow(0.99, (height - 1999)//10080)
POW_FUNC = lambda data: pack.IntType(256).unpack(__import__('blake_getpowhash').getPoWHash(data))
BLOCK_PERIOD = 300 # s
SYMBOL = 'UIS'
CONF_FILE_FUNC=lambda: os.path.join(os.path.join(os.environ['APPDATA'], 'unitus') if platform.system() == 'Windows' else os.path.expanduser('~/Library/Application Support/unitus/') if platform.system() == 'Darwin' else os.path.expanduser('~/.unitus'), 'unitus.conf')
BLOCK_EXPLORER_URL_PREFIX = 'http://explorer.unitus.info:1200/block/'
ADDRESS_EXPLORER_URL_PREFIX = 'http://explorer.unitus.info:1200/address/'
TX_EXPLORER_URL_PREFIX = 'http://explorer.unitus.info:1200/tx/'
SANE_TARGET_RANGE=(2**256//2**32//1000 - 1, 2**256//2**20 - 1)
DUMB_SCRYPT_DIFF = 1
DUST_THRESHOLD = 0.001e8
