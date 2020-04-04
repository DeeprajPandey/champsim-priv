'''
Plots the performance of the default branch predictors in ChampSim on different
trace files
'''
import matplotlib.pyplot as plt
import numpy as np


## LRU vs. FIFO
## order [605, 623, 607]
LRU = {    
    'ipc': [0.321602, 0.40567, 0.937681],
    'llc_avg_miss_latency': [159.922, 79.6715, 232.303], # in cycles
    'llc_total_hits': [1.172432, 0.993994, 2.634585],
    'llc_total_misses': [5.319085, 3.963356, 0.916776]
}

FIFO = {
    'ipc': [0.321041, 0.437748, 0.894465],
    'llc_avg_miss_latency': [155.6, 79.6332, 190.852], # in cycles
    'llc_total_hits': [1.036703, 1.932314, 2.363402],
    'llc_total_misses': [5.454814, 3.025036, 1.187961]
}

## No pref vs. Stream vs. Stream Modified
## order [623, 649, 654]
no_pref = {
    'ipc': [0.40567, 0.607586, 0.463109],
    'cycles': [4.93011515, 3.29171706, 4.31864078],
    'l1d_avg_miss_latency': [107.622, 148.411, 239.82],
    'l1d_ld_acc': [3.5557813, 2.6241016, 3.5949308],
    'l1d_ld_hits': [3.0536843, 2.3596902, 3.2764966],
    'l1d_ld_misses': [5.020970, 2.644114, 3.184342]
}

stream_mod = {
    'ipc': [0.493723, 0.944774, 0.572178],
    'cycles': [4.05085673, 2.11690810, 3.49541282],
    'l1d_avg_miss_latency': [102.814, 98.5577, 224.808],
    'l1d_ld_acc': [3.5781497, 2.7160217, 3.7548663],
    'l1d_ld_hits': [3.1910342, 2.5487631, 3.5428930],
    'l1d_ld_misses': [3.871155, 1.672586, 2.119733]
}

names_repl = ['605.mcf', '623.xalancbmk', '627.cam4']
names_pref = ['623.xalancbmk', '649.fotonik3d', '654.rom']

indices = np.arange(len(names_repl))
width = np.min(np.diff(indices))/3.

fig = plt.figure(dpi=120)
ax = fig.add_subplot(111)
lab_w = width/2.

rects_lru = ax.bar(indices-0.5*width/2., no_pref['l1d_ld_misses'], width=lab_w, color='#e4521b', label='no_prefetcher') #003f5c
rects_fifo = ax.bar(indices+0.5*width/2., stream_mod['l1d_ld_misses'], width=lab_w, color='#1a237e', label='mod_stream_pref') #7a5195
# rects603 = ax.bar(indices+0.5*width/4., bwaves['bp_rate'], width=lab_w, color='#', label='603-bwaves') #ef5675
# rects454 = ax.bar(indices+1.5*width/4., calculix['bp_rate'], width=lab_w, color='#', label='454-calculix') #ffa600


def autolabel(rects):
    """
    Attach a text label above each bar displaying its height
    """
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2., 1.05*height,
                '%.3f' % float(height),
                ha='center', va='bottom', fontsize='9', rotation=90)

autolabel(rects_lru)
autolabel(rects_fifo)
# autolabel(rects603)
# autolabel(rects454)


plt.ylim(0,7)

plt.legend(fontsize='x-small', loc='best')
plt.xticks(indices, names_repl)
plt.xlabel('Workloads', labelpad=5)
plt.ylabel('L1D Cache Load Misses (in millions)')

# plt.show()
plt.savefig('plot-results/ld_hits_pref.png', dpi=300,  bbox_inches='tight')
