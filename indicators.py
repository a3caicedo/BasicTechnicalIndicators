import pandas as pd

def SimpleMovingAverage(df, periods):
    sma = df.rolling(window=periods).mean()
    return sma

def ExponentialMovingAverage(df, span):
    ema = df.ewm(span=span,adjust=False).mean()
    return ema

def BollingerBands(df, periods, stds):
    bll = SimpleMovingAverage(df, periods)
    bll = bll.to_frame().rename(columns = {'Close':'BollingerCenter'})
    std = df.rolling(periods).std()
    bll['BollingerUp'] = bll['BollingerCenter'] + std * stds
    bll['BollingerDown'] = bll['BollingerCenter'] - std * stds
    return bll

def RelativeStrengthIndex(df, periods = 14, ema = True):
    close_delta = df.diff()
    up = close_delta.clip(lower=0)
    down = -1 * close_delta.clip(upper=0)
    if ema == True:
        ma_up = up.ewm(com = periods - 1, adjust=True, min_periods = periods).mean()
        ma_down = down.ewm(com = periods - 1, adjust=True, min_periods = periods).mean()
    else:
        ma_up = up.rolling(window = periods, adjust=False).mean()
        ma_down = down.rolling(window = periods, adjust=False).mean()
    rsi = ma_up / ma_down
    rsi = 100 - (100/(1 + rsi))
    return rsi

def MovingAverageConvergenceDivergence(data, slow, fast, smooth):
    exp1 = ExponentialMovingAverage(data, fast)
    exp2 = ExponentialMovingAverage(data, slow)
    macd = pd.DataFrame(exp1 - exp2).rename(columns = {'Close':'MACD'})
    signal = pd.DataFrame(macd.ewm(span = smooth, adjust = False).mean()).rename(columns = {'MACD':'Signal'})
    hist = pd.DataFrame(macd['MACD'] - signal['Signal']).rename(columns = {0:'hist'})
    frames =  [macd, signal, hist]
    df = pd.concat(frames, join = 'inner', axis = 1)
    return df