from __future__ import unicode_literals
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
plt.rcdefaults()
# prop = fm.FontProperties(fname='./OpenSansEmoji.ttf')
# plt.rcParams['font.family'] = prop.get_name()
# plt.rcParams['font.family'] = 'Apple Color Emoji'
# fm.ttfFontProperty('NotoColorEmoji')
# fm.createFontList(fm.OSXInstalledFonts(directories=None, fontext='ttf'), fontext='ttf')
# print(fm.OSXInstalledFonts(directories=None, fontext='ttf'))
# fm.findfont(prop, fontext='ttf', directory='./', fallback_to_default=True, rebuild_if_missing=True)
# plt.rcParams[emoji.fontset]='NotoColorEmoji.ttf'

imported='charts imported'

def createHistogram(emodicts):
    fig,ax=plt.subplots()

    emojis=emodicts.keys()
    y_pos=np.arange(len(emojis))
    performance=emodicts.values()

    ax.barh(y_pos,performance,xerr=0,align='center',color='gray',ecolor='black')
    ax.set_yticks(y_pos)
    ax.set_yticklabels(emojis)
    ax.invert_yaxis()
    ax.set_xlabel('Count')
    ax.set_title('Emoji Use Histogram')

    plt.show()
