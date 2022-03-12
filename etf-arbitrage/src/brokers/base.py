#!/usr/bin/env python3

from datetime import datetime
import backtrader as bt


class BrokerBase(bt.BackBroker):
    def __init__(self):
        super().__init__()
        self.log('*' * 5 + 'BASE BROKER INITIALIZED')

    def log(self, txt, dt=None):
        print('[BROKER] %s' % (txt))
