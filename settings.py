#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
App settings
'''

__doc__ = 'default application wide settings'

import sys
import os
import logging

from utils.common import getHomeDir, makeDir

USER_AGENT = APP_NAME = "Cryptonote Easy Miner"
VERSION = [0, 1, 'b1.3']

OPT_RANDOMIZE = False  # Randomize scan range start to reduce duplicates
OPT_SCANTIME = 60
OPT_REPLY_WITH_RPC2_EXPLICIT = True # support for explicit RPC 2.0 in reply
OPT_SEND_PING = True
OPT_PING_INTERVAL = 1 # Ping interval in second

HASHING_ALGO = ["Cryptonight", "Cryptonight-Light"]

_data_dir = str(makeDir(os.path.join(getHomeDir(), 'EvoMiner')))
DATA_DIR = _data_dir

log_file  = os.path.join(DATA_DIR, 'logs', 'evominer.log') # default logging file
log_level = logging.DEBUG # logging level