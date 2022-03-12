#!/usr/bin/env python3

from datetime import datetime
import backtrader as bt

from brokers.base import BrokerBase


class EtfArbitrageBroker(BrokerBase):
    def __init__(self):
        super().__init__()
        self.log('*' * 5 + 'ETF ARBITRAGE BROKER INITIALIZED')


