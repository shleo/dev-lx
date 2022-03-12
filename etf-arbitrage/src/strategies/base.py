#!/usr/bin/env python3

from datetime import datetime
import backtrader as bt


class StrategyBase(bt.Strategy):
    def __init__(self):
        super().__init__()
        self.log('*' * 5 + 'BASE STRATEGY INITIALIZED')

    def prenext(self):
        self.log('*' * 5 + 'BEFORE MATURE')

    def stop(self):
        self.log('*' * 5 + 'BASE STRATEGY STOPPED')

    def log(self, txt, dt=None):
        dt = dt or self.datas[0].datetime.date(0)
        print('[%s] %s' % (dt.isoformat(), txt))
