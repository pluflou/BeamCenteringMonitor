#BCM analysis
#Author: Sara Ayoub
#Date: February 10 2019		
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mt
import datetime
from negativecurrents import negativePlates

from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

##import data ##
data=pd.read_csv('data/BCManalysis', comment='#', sep='\t', names=["Time", "TL", "TL Neg Error", "TL Pos Error", "TR", "TR Neg Error", "TR Pos Error", "BL", "BL Neg Error", "BL Pos Error", "BR", "BR Neg Error", "BR Pos Error", "B1 Current", "Current Neg Error", "Current Pos Error"])
data=data.dropna()
tl, tr, bl, br, current = np.array(data["TL"]),np.array(data["TR"]),np.array(data["BL"]),np.array(data["BR"]), np.array(data["B1 Current"])
e1p, e1n, e2p,e2n,e3p,e3n,e4p,e4n= data["TL Pos Error"],data["TL Neg Error"],data["TR Pos Error"],data["TR Neg Error"],data["BL Pos Error"],data["BL Neg Error"],data["BR Pos Error"],data["BR Neg Error"],
################

#Parsing CS-S timestamps for plotting (need to use plot_dates for this format)
fmt = '%Y-%m-%d %H:%M:%S'
time = mt.dates.date2num([datetime.datetime.strptime(row[:-10], fmt) for row in data["Time"]])

#tranpose of errors is needed to match data
err1= np.transpose(np.array([e1p,e1n]))
err2=np.transpose( np.array([e2p, e2n]))
err3= np.transpose(np.array([e3p, e3n]))
err4= np.transpose(np.array([e4p, e4n]))

#Getting rid of negative currents plate by plate
TL, TR, BL, BR, E1, E2, E3, E4= negativePlates(tl, tr, bl, br, err1, err2, err3, err4)

total= abs(TL)+ abs(TR)+abs(BL)+abs(BR)

sumL= (TL+BL)/total
sumR= (TR+BR)/total

ratio= sumL/sumR
for i in range(len(ratio)): #these values are not interesting to us anyway
    if (ratio[i]>1E3):
        ratio[i]=0

#propagating uncertainty from linear interpolation to the ratio
err_total= E1+E2+E3+E4

errL0= sumL*(((E1[:,0]+E3[:,0])/(TL+BL))+(err_total[:,0]/total))
errL1= sumL*(((E1[:,1]+E3[:,1])/(TL+BL))+(err_total[:,1]/total))
errL= [errL0,errL1]

errR= [sumR*((E2[:,0]+E4[:,0])/(TR+BR)+(err_total[:,0]/total)),
       sumR*((E2[:,1]+E4[:,1])/(TR+BR)+(err_total[:,1]/total))]

err_ratio_p=ratio*((errL[0]/sumL) + (errR[0]/sumR))
err_ratio_n= ratio*((errL[1]/sumL) + (errR[1]/sumR))


##Plotting results##
fig = plt.figure()
ax1 = fig.add_axes([0.1, 0.6, 0.8, 0.25], ylim=(-0.1, 1.2))
ax2 = fig.add_axes([0.1, 0.35, 0.8, 0.25], ylim=(-0.5, 10))
ax3 = fig.add_axes([0.1, 0.1, 0.8, 0.25])


ax1.fill_between(time, sumL-errL[1], sumL+errL[0],facecolor='b',alpha=0.2)
ax1.fill_between(time, sumR-errR[1], sumR+errR[0],facecolor='orange',alpha=0.2)
ax1.plot_date(time,sumL, color="blue", label="Left Sum", markersize=3)
ax1.plot_date(time, sumR, color="orange", label="Right Sum" , markersize=3)
ax1.set_ylabel('Normalized BCM Current')
ax1.set_ylim=(-0.1, 1.2)
ax1.legend()

ax2.plot_date(time, ratio, label="Ratio Left/Right" , markersize=3)
ax2.fill_between(time,ratio-err_ratio_n, ratio+err_ratio_p, facecolor='blue',alpha=0.2)
line= [1  for i in range(len(time))]
ax2.plot(time, line, color="red")
ax2.set_ylim=(-0.5, 10)
ax2.set_ylabel('Ratio L/R')
ax2.legend()


ax3.plot_date(time, current, label="Dipole Current", color="blue", markersize=3)
ax3.set_ylabel('B1 Current (A)')
ax3.legend()

plt.show()
##################

