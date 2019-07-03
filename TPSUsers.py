#!/usr/bin/env python2
import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(189.6,100.0))
fig, ax1 = plt.subplots()

#Give x and y samples to plot
ax1.plot([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120],[0,84,246,410,558,738,903,1040,1221,1368,1504,1681,1814,1909,2239,2186,2334,2475,2906,2783,2998,3131,3300,3551,3331,3542,3856,3749,3923,4124,4622,4572,4895,4741,5062,5195,5209,5682,5405,5538,5386,5430,5494,6367,6118,6587,6567,5370,5502,5573,5731,5522,5449,6939,7178,7272,7630,7158,6613,5877,7575,8754,7559,6949,7293,7746,8297,6810,6925,7334,6745,7189,9107,8380,6827,7548,7628,7622,6580,8358,6842,7833,7456,8207,8699,7319,7440,7613,8098,7663,7692,7614,8612,7219,8877,7163,7919,8153,6399,8338,8026,8519,7180,8610,7831,8434,8661,6738,7594,9077,7357,8765,7155,7935,9487,7965,7215,8402,8154,8370,7416],color='blue')

#Set labels
ax1.set_xlabel('Time', fontsize=20)
ax1.tick_params(axis='y', labelcolor='blue',labelsize=15)
ax1.tick_params(axis='x',labelsize=15)
plt.legend(['QPS'], loc='upper left',fontsize=15)

#Set xlimit and ylimits
plt.ylim((0,10000))
plt.xlim((0,120))

#Customize x axis values using xticks
x=["0","10S","20S","30S","40S","50S","60S","70S","80S","90S","10S","110S","120S"]
l=[00,10,20,30,40,50,60,70,80,90,100,110,120]
plt.xticks(l,x)

#Take another subplot
ax2 = ax1.twinx()

#Give x and y samples to plot
ax2.plot([0,15,30,45,60,75,90,105,120],[0,250,500,750,1000,1250,1500,1750,2000],color='red')
ax2.tick_params(axis='y', labelcolor='red', pad=1,labelsize=15)

#Set labels
ax2.set_ylabel('Users', fontsize=20,color='red')
ax2.set_ylim(0,2000)

plt.show()