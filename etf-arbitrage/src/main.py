from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

import datetime  # For datetime objects
import os.path  # To manage paths
import sys  # To find out the script name (in argv[0])

# Import the backtrader platform
import backtrader as bt

# Import local components
from feeds.stock_feed import StockFeed
from strategies.simple_strategy import SimpleStrategy
from brokers.etf_arbitrage_broker import EtfArbitrageBroker

if __name__ == '__main__':
    # Create a cerebro entity
    cerebro = bt.Cerebro()

    # Add a broker
    cerebro.broker = EtfArbitrageBroker()

    # Add a strategy
    cerebro.addstrategy(SimpleStrategy)

    # Datas are in a subfolder of the samples. Need to find where the script is
    # because it could have been called from anywhere
    modpath = os.path.dirname(os.path.abspath(sys.argv[0]))
    datapath1 = os.path.join(
        modpath, '../../../etf-arbitrage-data/ETF_2021-11-15/all_stock_data/stock_000001.XSHE_2021-11-15.csv')
    datapath2 = os.path.join(
        modpath, '../../../etf-arbitrage-data/ETF_2021-11-15/all_stock_data/stock_000002.XSHE_2021-11-15.csv')

    # Create a Data Feed
    data1 = StockFeed(
        dataname=datapath1,
        timeframe=bt.TimeFrame.Seconds)
    data2 = StockFeed(
        dataname=datapath2,
        timeframe=bt.TimeFrame.Seconds)

    # Add the Data Feed to Cerebro
    cerebro.adddata(data1, name="000001.XSHE")
    cerebro.adddata(data2, name="000002.XSHE")

    # Set our desired cash start
    cerebro.broker.setcash(100000.0)

    # 0.1% ... divide by 100 to remove the %
    cerebro.broker.setcommission(commission=0.001)

    # Print out the starting conditions
    print('Starting Portfolio Value: %.2f' % cerebro.broker.getvalue())

    # Run over everything
    cerebro.run()

    # Print out the final result
    print('Final Portfolio Value: %.2f' % cerebro.broker.getvalue())
