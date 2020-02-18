'''
Plots the performance of the default branch predictors in ChampSim on different
trace files
'''
import matplotlib.pyplot as plt
import numpy as np


#649
fotonik3d = {
    'bp_rate': [98.2442, 99.0743, 99.8778],
    'ipc': [1.12551, 1.14527, 1.21002]
    }
#654
roms = {
    'bp_rate': [97.92, 98.1034, 99.8879],
    'ipc': [1.34445, 1.3579, 1.56185]
    }
#603
bwaves = {
    'bp_rate': [93.5709, 91.48, 99.8845],
    'ipc': [1.28696, 1.23661, 1.52121]
    }
#454
calculix = {
    'bp_rate': [96.8821, 96.9555, 99.6659],
    'ipc': [1.81517, 1.81835, 1.91448]
    }

names = ['gshare', 'percep', 'hashed-percep']

indices = np.arange(len(names))
width = np.min(np.diff(indices))/3.

fig = plt.figure(dpi=120)
ax = fig.add_subplot(111)
lab_w = width/4.

rects649 = ax.bar(indices-1.5*width/4., fotonik3d['bp_rate'], width=lab_w, color='#003f5c', label='649-fotonik3d')
rects654 = ax.bar(indices-0.5*width/4., roms['bp_rate'], width=lab_w, color='#7a5195', label='654-roms')
rects603 = ax.bar(indices+0.5*width/4., bwaves['bp_rate'], width=lab_w, color='#ef5675', label='603-bwaves')
rects454 = ax.bar(indices+1.5*width/4., calculix['bp_rate'], width=lab_w, color='#ffa600', label='454-calculix')


def autolabel(rects):
    """
    Attach a text label above each bar displaying its height
    """
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2., 1.05*height,
                '%.3f' % float(height),
                ha='center', va='bottom', fontsize='7', rotation=90)

autolabel(rects649)
autolabel(rects654)
autolabel(rects603)
autolabel(rects454)


plt.ylim(0,150)

plt.legend(fontsize='x-small')
plt.xticks(indices, names)
plt.xlabel('branch predictors', labelpad=5)
plt.ylabel('prediction percentage (success)')

plt.show()
#plt.savefig('plot-results/pred_percent.png', dpi=300,  bbox_inches='tight')
