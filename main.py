import pandas as pd
from binance.client import Client
from time import sleep
from indicators import *
from binanceutils import *
from plotutils import *

apiKey = "apiKey"
apiSecret = "apiSecret"
client = Client(apiKey, apiSecret)

initializePlot()

df = getTodayData(client, "ETHUSDT", 6)

df['EMA200'] = SimpleMovingAverage(df['Close'], 100)
macd = MovingAverageConvergenceDivergence(df['Close'], 26, 12, 9)
bollinger = BollingerBands(df['Close'], 20, 2)
df = pd.concat([df, macd], axis=1)
df = pd.concat([df, bollinger], axis=1)
Image = plotIndicators(df[-60:])
Image.save("resultado.png", "PNG", quality=100, optimize=True, progressive=True)