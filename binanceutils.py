import datetime
import pandas as pd

def getTodayData(client, symbol, hours):
    finalDate = datetime.datetime.utcnow()
    initialDate = finalDate - datetime.timedelta(hours = hours)
    df = client.get_historical_klines(symbol, client.KLINE_INTERVAL_1MINUTE, str(initialDate), str(finalDate))
    df = pd.DataFrame(df, columns=['Open time', 'Open', 'High', 'Low', 'Close', 'Volume', 'Close time', 'Quote asset volume', 'Number of trades', 'Taker buy base asset volume', 'Taker buy quote asset volume', 'Can be ignored'])
    df.drop(columns=['Open time', 'Open', 'High', 'Low', 'Quote asset volume', 'Number of trades', 'Taker buy base asset volume', 'Taker buy quote asset volume', 'Can be ignored'], inplace=True)
    df['Close time'] = pd.to_datetime(df['Close time'], unit='ms')
    df.set_index('Close time', inplace=True)
    df['Close'] = df['Close'].astype(float)
    df['Volume'] = df['Volume'].astype(float)
    return df 