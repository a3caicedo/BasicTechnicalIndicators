import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from PIL import Image

def initializePlot():

    global ax, fig
    
    fig, ax = plt.subplots(nrows=2, ncols=1, sharex=True, figsize=(8, 6))
    fig.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1)
    gs = gridspec.GridSpec(2, 1)
    gs.update(wspace=0, hspace=0)

    ax[0] = plt.subplot(gs[0])
    ax[0].spines['top'].set_visible(False)
    ax[0].spines['right'].set_visible(False)
    ax[0].spines['bottom'].set_visible(False)
    ax[0].spines['left'].set_visible(False)
    ax[0].get_xaxis().set_visible(False)
    ax[0].get_yaxis().set_visible(False)
    ax[0].set_facecolor('#ffffff')

    ax[1] = plt.subplot(gs[1])
    ax[1].spines['top'].set_visible(False)
    ax[1].spines['right'].set_visible(False)
    ax[1].spines['bottom'].set_visible(False)
    ax[1].spines['left'].set_visible(False)
    #ax[1].get_xaxis().set_visible(False)
    ax[1].get_yaxis().set_visible(False)
    ax[1].set_facecolor('#ffffff')


def plotIndicators(df):

    global ax, fig
    
    ax[0].plot(df['Close'],color = '#000000',linewidth=3)
    ax[0].plot(df['EMA200'],label='EMA200',color = '#ffeb3b',linewidth=2)

    ax[0].plot(df['BollingerCenter'],color = '#00ff00',linewidth=1, linestyle='dashed')
    ax[0].plot(df['BollingerUp'],color = '#ff0000',linewidth=1, linestyle='dashed')
    ax[0].plot(df['BollingerDown'],color = '#ff0000',linewidth=1, linestyle='dashed')
    
    ax[1].plot(df['MACD'], color = '#2962FF', linewidth=1)
    ax[1].plot(df['Signal'], color = '#FF6D00', linewidth=1)
    for i in range(len(df['Close'])):
        color = '#FF5252' if df['hist'][i] < 0 else '#26A69A'
        ax[1].bar(df.index[i], df['hist'][i], color=color, width=0.0005)
    fig.canvas.draw()

    return Image.frombytes('RGB', fig.canvas.get_width_height(), fig.canvas.tostring_rgb())