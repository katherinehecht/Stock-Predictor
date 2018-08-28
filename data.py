# https://www.youtube.com/watch?v=JcI5Vnw0b2c&index=2&list=PLQVvvaa0QuDfKTOs3Keq_kaG2P55YRn5v

import pandas as pd
import Quandl
import math

df = Quandal.get('WIKI/GOOGL')

# Features
df = df[['Adj. Open','Adj.High','Adj. Low','Adj. Close','Adj. Volume']]
df['HL_PCT']=(df['Adj. High'] - df['Adj. Close'] )  / df['Adj. Close'] * 100.0
df['PCT_change']=(df['Adj. Close'] - df['Adj. Open'] )  / df['Adj. Open'] * 100.0

df = df[['Adj. Close', 'HL_PCT', 'PCT_change','Adj. Volume']]i

forecast_col = 'Adj. Close'

df.fillna('-9999', inplace=True) # fill in absent data

forecast_out = int(math.ceil(0.1*len(df)))


# Labels
df['label'] = df[forecast_col].shift(-forecast_out)


