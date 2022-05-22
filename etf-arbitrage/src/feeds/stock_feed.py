import backtrader.feeds as btfeed


class StockFeed(btfeed.GenericCSVData):
    params = (
        ('dtformat', '%Y-%m-%d %H:%M:%S'),
        ('datetime', 1),
        ('open', 4),
        ('high', 5),
        ('low', 6),
        ('close', 4),
        ('volume', 8),
        ('openinterest', -1)
    )
