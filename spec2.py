import numpy as np
from scipy import loadtxt, optimize
import matplotlib.pyplot as plt

# Here we define our fit function and residual functions
def fitfunc(p, x):
    return p[0]*x + p[1]
def residual(p, x, y, dy):
    return (fitfunc(p, x)-y)/dy

# Read in the data from file
t,V,t2,V2= loadtxt('/home/alemsolobog/Exper9/aj_data/day2_6ish', unpack=True, skiprows=1)
f = t * 61640625000
df = t * 1518845239.0549629
##############################################################################
# Fit
##############################################################################
# p01 = [10,6]
# pf1, cov1, info1, mesg1, success1 = optimize.leastsq(residual, p01,
#                                      args = (E, ch, dch), full_output=1)
#
# if cov1 is None:
#     print('Fit did not converge')
#     print('Success code:', success1)
#     print(mesg1)
# else:
#     print('Fit Converged')
#     chisq1 = sum(info1['fvec']*info1['fvec'])
#     dof1 = len(E)-len(pf1)
#     pferr1 = [np.sqrt(cov1[i,i]) for i in range(len(pf1))]
#     print('Converged with chi-squared', chisq1)
#     print('Number of degrees of freedom, dof =',dof1)
#     print('Reduced chi-squared:', chisq1/dof1)
#     print('Inital guess values:')
#     print('  p0 =', p01)
#     print('Best fit values:')
#     print('  pf =', pf1)
#     print('Uncertainties in the best fit values:')
#     print('  pferr =', pferr1)
#     print()

fig1 = plt.figure()
ax1 = fig1.add_subplot(111)
#ax1.errorbar(f, V, xerr =df, fmt='k.', label = 'Data')
#ax1.set_xlabel('Frequency, $f$ $(Hz)$')
#ax1.set_xlim(f.min(),f.max())

ax1.set_xlabel('Time, $t$ $(sec)$')
ax1.errorbar(t, V, fmt='k.', label = 'Data')
ax1.set_title('Calibration Data from Michelson Interferometer')


ax1.set_ylabel('Voltage, $V$ $(V)$')
ax1.legend()

ax1.legend(loc='lower right')
# ax1.text(0.02, .95, textfit, transform=ax1.transAxes, fontsize=12,
#         verticalalignment='top')


plt.savefig('dfs_t.png')
#plt.show()
