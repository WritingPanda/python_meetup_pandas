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
AAPL.to_csv('../data/AAPL.csv', index_col='Date', parse_dates=True)

# Microsoft
MSFT = pd.io.data.get_data_yahoo('MSFT',
                                 start=datetime.datetime(2000, 7, 1),
                                 end=datetime.datetime(2015, 7, 1))
MSFT.to_csv('../data/MSFT.csv', index_col='Date', parse_dates=True)

# Google
GOOG = pd.io.data.get_data_yahoo('GOOG',
                                 start=datetime.datetime(2000, 7, 1),
                                 end=datetime.datetime(2015, 7, 1))
GOOG.to_csv('../data/GOOG.csv', index_col='Date', parse_dates=True)

# Tesla
TSLA = pd.io.data.get_data_yahoo('TSLA',
                                 start=datetime.datetime(2000, 7, 1),
                                 end=datetime.datetime(2015, 7, 1))
TSLA.to_csv('../data/TSLA.csv', index_col='Date', parse_dates=True)

# Wells Fargo
WFC = pd.io.data.get_data_yahoo('WFC',
                                start=datetime.datetime(2000, 7, 1),
                                end=datetime.datetime(2015, 7, 1))
WFC.to_csv('../data/WFC.csv', index_col='Date', parse_dates=True)

# J.P. Morgan
JPM = pd.io.data.get_data_yahoo('JPM',
                                start=datetime.datetime(2000, 7, 1),
                                end=datetime.datetime(2015, 7, 1))
JPM.to_csv('../data/JPM.csv', index_col='Date', parse_dates=True)

# Citi Group
C = pd.io.data.get_data_yahoo('C',
                              start=datetime.datetime(2000, 7, 1),
                              end=datetime.datetime(2015, 7, 1))
C.to_csv('../data/C.csv', index_col='Date', parse_dates=True)

# Bank of America
BAC = pd.io.data.get_data_yahoo('BAC',
                                start=datetime.datetime(2000, 7, 1),
                                end=datetime.datetime(2015, 7, 1))
BAC.to_csv('../data/BAC.csv', index_col='Date', parse_dates=True)

# BB&T
BBT = pd.io.data.get_data_yahoo('BBT',
                                start=datetime.datetime(2000, 7, 1),
                                end=datetime.datetime(2015, 7, 1))
BBT.to_csv('../data/BBT.csv', index_col='Date', parse_dates=True)

# J&J Snack Foods Corp
JJSF = pd.io.data.get_data_yahoo('JJSF',
                                 start=datetime.datetime(2000, 7, 1),
                                 end=datetime.datetime(2015, 7, 1))
JJSF.to_csv('../data/JJSF.csv', index_col='Date', parse_dates=True)

# Tyson Foods, Inc.
TSN = pd.io.data.get_data_yahoo('TSN',
                                start=datetime.datetime(2000, 7, 1),
                                end=datetime.datetime(2015, 7, 1))
TSN.to_csv('../data/TSN.csv', index_col='Date', parse_dates=True)

# General Mills
GIS = pd.io.data.get_data_yahoo('GIS',
                                start=datetime.datetime(2000, 7, 1),
                                end=datetime.datetime(2015, 7, 1))
GIS.to_csv('../data/GIS.csv', index_col='Date', parse_dates=True)

# Hormel Foods Corporation
HRL = pd.io.data.get_data_yahoo('HRL',
                                start=datetime.datetime(2000, 7, 1),
                                end=datetime.datetime(2015, 7, 1))
HRL.to_csv('../data/HRL.csv', index_col='Date', parse_dates=True)

# Mead Johnson Nutrition Company
MJN = pd.io.data.get_data_yahoo('MJN',
                                start=datetime.datetime(2000, 7, 1),
                                end=datetime.datetime(2015, 7, 1))
MJN.to_csv('../data/MJN.csv', index_col='Date', parse_dates=True)

# Palo Alto Networks, Inc.
PANW = pd.io.data.get_data_yahoo('PANW',
                                 start=datetime.datetime(2000, 7, 1),
                                 end=datetime.datetime(2015, 7, 1))
PANW.to_csv('../data/PANW.csv', index_col='Date', parse_dates=True)

# Fortinet Inc.
FTNT = pd.io.data.get_data_yahoo('FTNT',
                                 start=datetime.datetime(2000, 7, 1),
                                 end=datetime.datetime(2015, 7, 1))
FTNT.to_csv('../data/FTNT.csv', index_col='Date', parse_dates=True)

# Symantec
SYMC = pd.io.data.get_data_yahoo('SYMC',
                                 start=datetime.datetime(2000, 7, 1),
                                 end=datetime.datetime(2015, 7, 1))
SYMC.to_csv('../data/SYMC.csv', index_col='Date', parse_dates=True)

# Cisco
CSCO = pd.io.data.get_data_yahoo('CSCO',
                                 start=datetime.datetime(2000, 7, 1),
                                 end=datetime.datetime(2015, 7, 1))
CSCO.to_csv('../data/CSCO.csv', index_col='Date', parse_dates=True)

# Check Point Software Technologies Ltd.
CHKP = pd.io.data.get_data_yahoo('CHKP',
                                 start=datetime.datetime(2000, 7, 1),
                                 end=datetime.datetime(2015, 7, 1))
CHKP.to_csv('../data/CHKP.csv', index_col='Date', parse_dates=True)

