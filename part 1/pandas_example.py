import pandas as pd
import pandas.io.data
import datetime

tech_stocks = ('AAPL', 'MSFT', 'GOOG', 'FB', 'TSLA',)
bank_stocks = ('WFC', 'JPM', 'C', 'BAC', 'BBT',)
food_stocks = ('JJSF', 'TSN', 'GIS', 'HRL', 'MJN',)
cybersec_stocks = ('PANW', 'FTNT', 'SYMC', 'CSCO', 'CHKP',)

# Apple Computers
AAPL = pd.io.data.get_data_yahoo('AAPL',
                                 start=datetime.datetime(2000, 7, 1),
                                 end=datetime.datetime(2015, 7, 1))
# Microsoft
MSFT = pd.io.data.get_data_yahoo('MSFT',
                                 start=datetime.datetime(2000, 7, 1),
                                 end=datetime.datetime(2015, 7, 1))
# Google
GOOG = pd.io.data.get_data_yahoo('GOOG',
                                 start=datetime.datetime(2000, 7, 1),
                                 end=datetime.datetime(2015, 7, 1))
# Tesla
TSLA = pd.io.data.get_data_yahoo('TSLA',
                                 start=datetime.datetime(2000, 7, 1),
                                 end=datetime.datetime(2015, 7, 1))
# Wells Fargo
WFC = pd.io.data.get_data_yahoo('WFC',
                                start=datetime.datetime(2000, 7, 1),
                                end=datetime.datetime(2015, 7, 1))
# J.P. Morgan
JPM = pd.io.data.get_data_yahoo('JPM',
                                start=datetime.datetime(2000, 7, 1),
                                end=datetime.datetime(2015, 7, 1))
# Citi Group
C = pd.io.data.get_data_yahoo('C',
                              start=datetime.datetime(2000, 7, 1),
                              end=datetime.datetime(2015, 7, 1))
# Bank of America
BAC = pd.io.data.get_data_yahoo('BAC',
                                start=datetime.datetime(2000, 7, 1),
                                end=datetime.datetime(2015, 7, 1))
# BB&T
BBT = pd.io.data.get_data_yahoo('BBT',
                                start=datetime.datetime(2000, 7, 1),
                                end=datetime.datetime(2015, 7, 1))
# J&J Snack Foods Corp
JJSF = pd.io.data.get_data_yahoo('JJSF',
                                 start=datetime.datetime(2000, 7, 1),
                                 end=datetime.datetime(2015, 7, 1))
# Tyson Foods, Inc.
TSN = pd.io.data.get_data_yahoo('',
                                start=datetime.datetime(2000, 7, 1),
                                end=datetime.datetime(2015, 7, 1))
# General Mills
GIS = pd.io.data.get_data_yahoo('TSN',
                                start=datetime.datetime(2000, 7, 1),
                                end=datetime.datetime(2015, 7, 1))
# Hormel Foods Corporation
HRL = pd.io.data.get_data_yahoo('HRL',
                                start=datetime.datetime(2000, 7, 1),
                                end=datetime.datetime(2015, 7, 1))
# Mead Johnson Nutrition Company
MJN = pd.io.data.get_data_yahoo('MJN',
                                start=datetime.datetime(2000, 7, 1),
                                end=datetime.datetime(2015, 7, 1))
# Palo Alto Networks, Inc.
PANW = pd.io.data.get_data_yahoo('PANW',
                                 start=datetime.datetime(2000, 7, 1),
                                 end=datetime.datetime(2015, 7, 1))
# Fortinet Inc.
FTNT = pd.io.data.get_data_yahoo('FTNT',
                                 start=datetime.datetime(2000, 7, 1),
                                 end=datetime.datetime(2015, 7, 1))
# Symantec
SYMC = pd.io.data.get_data_yahoo('SYMC',
                                 start=datetime.datetime(2000, 7, 1),
                                 end=datetime.datetime(2015, 7, 1))
# Cisco
CSCO = pd.io.data.get_data_yahoo('CSCO',
                                 start=datetime.datetime(2000, 7, 1),
                                 end=datetime.datetime(2015, 7, 1))
# Check Point Software Technologies Ltd.
CHKP = pd.io.data.get_data_yahoo('CHKP',
                                 start=datetime.datetime(2000, 7, 1),
                                 end=datetime.datetime(2015, 7, 1))
