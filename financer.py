import datetime as dt
import matplotlib.pyplot as pyplot
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web

style.use('ggplot')
start = dt.datetime(2001,1,1)
end = dt.datetime(2016,12,31)

df = web.DataReader('TSLA' , 'yahoo', start , end)
# head shows first entries
print(df.head(10))
# tail shows last entries
print(df.tail(10))
