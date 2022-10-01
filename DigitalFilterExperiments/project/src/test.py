import matplotlib.pyplot as plt
import numpy as np

file = open("biceps_leandro.txt", 'r')

emg = []
for line in file.readlines():
    emg.append(int(line))


emg = np.array(emg)
emg = emg - np.mean(emg)
emg = np.abs(emg)
emg_low_pass = []
n = 64
for i in range(len(emg) - n):
    emg_low_pass.append(np.mean(emg[i:i+n]))

plt.plot(emg_low_pass)
plt.show()
