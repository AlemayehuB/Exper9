import numpy as np
from scipy import loadtxt, optimize
import matplotlib.pyplot as plt

# Here we define our fit function and residual functions
def fitfunc(p, x):
    return p[0]*x + p[1]
def residual(p, x, y, dy):
    return (fitfunc(p, x)-y)/dy

# Read in the data from file
t,V,t2,V2= loadtxt('/home/alemsolobog/Exper9/aj_data/day2_peaks', unpack=True, skiprows=1)


fig1 = plt.figure()
ax1 = fig1.add_subplot(111)
f = t * 61640625000
df = t * 1518845239.0549629
#ax1.errorbar(f, V, xerr = df, fmt='k.', label = 'Data')
ax1.errorbar(t, V, fmt='k.', label = 'Data')
#T = np.linspace(E.min(), E.max(), 500)
#ax1.plot(t, V, 'r-', label = 'Data')
#ax1.set_xlim(f.min(),f.max())

ax1.set_title('Calibration Data from Michelson Interferometer')
ax1.set_xlabel('Time, $t$ $(sec)$')
ax1.set_xlabel('Frequency, $f$ $(Hz)$')
ax1.set_ylabel('Voltage, $V$ $(V)$')
ax1.legend()


plt.savefig('dbs_t.png')
#plt.show()
