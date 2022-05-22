#!/usr/bin/env python3

import backtrader as bt

from strategies.base import StrategyBase


class SimpleStrategy(StrategyBase):
    def __init__(self):
        super().__init__()

        # Initialize member variables
        self.order = None

        # Keep a reference to the "close" line in the data[0] dataseries
        self.dataclose = {}
        self.sma = {}
        for data in self.datas:
            self.dataclose[data._name] = data.close
            self.sma[data._name] = bt.indicators.SimpleMovingAverage(
                data, period=15)
        self.log('*' * 5 + 'SIMPLE STRATEGY INITIALIZED')

    def notify_order(self, order):
        if order.status in [order.Submitted, order.Accepted]:
            # Buy/Sell order submitted/accepted to/by broker - Nothing to do
            return

        # Check if an order has been completed
        # Attention: broker could reject order if not enough cash
        if order.status in [order.Completed]:
            if order.isbuy():
                self.log(
                    'BUY EXECUTED, Price: %.2f, Cost: %.2f, Comm %.2f' %
                    (order.executed.price,
                     order.executed.value,
                     order.executed.comm))

            else:  # Sell
                self.log('SELL EXECUTED, Price: %.2f, Cost: %.2f, Comm %.2f' %
                         (order.executed.price,
                          order.executed.value,
                          order.executed.comm))

        elif order.status in [order.Canceled, order.Margin, order.Rejected]:
            self.log('Order Canceled/Margin/Rejected')

        self.order = None

    def next(self):
        StrategyBase.next(self)

        for data in self.datas:
            name = data._name

            # Simply log the closing price of the series from the reference
            self.log('Name: %s, Close, %.2f : SMA, %.2f' %
                     (name, self.dataclose[name][0], self.sma[name][0]))

            # Check if an order is pending ... if yes, we cannot send a 2nd one
            if self.order:
                return

            for position in self.positions:
                self.log('Position: [%s %d]' %
                         (position._name, self.positions[position].size))
            self.log('Cash: %.2f' % self.broker.cash)

            # Check if we are in the market
            if name not in self.positions or self.positions[name].size <= 0:

                # Not yet ... we MIGHT BUY if ...
                if self.dataclose[name][0] > self.sma[name][0]:

                    # BUY, BUY, BUY!!! (with all possible default parameters)
                    self.log('Name: %s, BUY CREATE, %.2f' %
                             (name, self.dataclose[name][0]))

                    # Keep track of the created order to avoid a 2nd order
                    self.order = self.buy(data)

            else:

                if self.dataclose[name][0] < self.sma[name][0]:
                    # SELL, SELL, SELL!!! (with all possible default parameters)
                    self.log('Name: %s, SELL CREATE, %.2f' %
                             (name, self.dataclose[name][0]))

                    # Keep track of the created order to avoid a 2nd order
                    self.order = self.sell(data)
