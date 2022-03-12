#!/usr/bin/env python3

from datetime import datetime
import backtrader as bt

from brokers.base import BrokerBase


class EtfArbitrageBroker(BrokerBase):

    etf_to_basket = {
        'TEST_ETF': {
            'size': 100,
            'basket': {
                'stocks': {
                    'TEST_STOCK_1': 20,
                    'TEST_STOCK_2': 30,
                },
                'cash': 15,
            }
        }
    }

    def __init__(self):
        super().__init__()
        self.log('*' * 5 + 'ETF ARBITRAGE BROKER INITIALIZED')
    
    def create_etf(self, etf):
        # Preliminary checks
        if (etf not in self.etf_to_basket):
            self.log('ETF %s creation: ERROR: Unable to find ETF in arbitrage dictionary!' % (etf))
            return
        basket = self.etf_to_basket[etf]['basket']
        size = self.etf_to_basket[etf]['size']
        cash = basket['cash']
        if (self.cash < cash):
            self.log('ETF %s creation ERROR: Insufficient cash: %f less than required amount %f' % (etf, self.cash, cash))
        stocks = basket['stocks']
        for stock_name in stocks:
            stock_size = stocks[stock_name]
            if (stock_name not in self.positions):
                self.log('ETF %s creation ERROR: ETF basket stock %s not owned' % (etf, stock_name))
                return
            stock_size_owned = self.positions[stock_name].size
            if (stock_size_owned < stock_size):
                self.log('ETF %s creation ERROR: ETF basket stock %s insufficient amount: %f less than required amount %f' % (etf, stock_name, stock_size_owned, stock_size))
        
        # Execution
        self.cash -= cash
        self.log('ETF %s creation: spent %f cash' % (etf, cash))
        for stock_name in stocks:
            stock_size = stocks[stock_name]
            self.log('ETF %s creation: spent %d %s shares' % (etf, stock_size, stock_name))
            self.positions[stock_name].size -= stocks[stock_name]
        
        # TODO: Create ETF position
        self.log('ETF %s creation: Gained %d ETF shares' % (etf))

    def redeem_etf(self, etf):
        # Preliminary checks
        if (etf not in self.etf_to_basket):
            self.log('ETF %s redemption ERROR: Unable to find ETF in arbitrage dictionary!' % (etf))
            return
        if (etf not in self.positions):
            self.log('ETF %s redemption ERROR: Unable to find ETF in positions!' % (etf))
        # TODO: More checks and redemption


