import numpy as np
from scipy import loadtxt, optimize
import matplotlib.pyplot as plt

# Here we define our fit function and residual functions
def fitfunc(p, x):
    return p[0]*x + p[1]
def residual(p, x, y, dy):
    return (fitfunc(p, x)-y)/dy

# Read in the data from file
t,V,t2,V2= loadtxt('/home/alemsolobog/Exper9/aj_data/calib_day2', unpack=True, skiprows=1)

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
#ax1.errorbar(E, ch, dch, fmt='k.', label = 'Data')
#T = np.linspace(E.min(), E.max(), 500)
ax1.plot(t, V, 'r-', label = 'Data')

ax1.set_title('Calibration Data from Michelson Interferometer')
ax1.set_xlabel('Time, $t$ $(sec)$')
ax1.set_ylabel('Voltage, $V$ $(V)$')
ax1.legend()

textstr1 = "$\\Delta t_{1}$"
textstr2 = "$\\Delta t_{2}$"
textstr3 = "$\\Delta t_{3}$"
textstr4 = "$\\Delta t_{4}$"
textstr5 = "$\\Delta t_{5}$"
textstr6 = "$\\Delta t_{6}$"
textstr7 = "$\\Delta t_{7}$"

ax1.annotate("", xy=(0.0775,0.069), xytext=(0.0905, 0.069),arrowprops={'arrowstyle': '<->'},va='center')
ax1.annotate(textstr1, xy=(0.0810, 0.070))
ax1.annotate("", xy=(0.0895,0.0855), xytext=(0.1025, 0.0855),arrowprops={'arrowstyle': '<->'},va='center')
ax1.annotate(textstr2, xy=(0.0930, 0.086))
ax1.annotate("", xy=(0.1015, 0.09755), xytext=(0.1130,0.0975),arrowprops={'arrowstyle': '<->'},va='center')
ax1.annotate(textstr3, xy=(0.1054, 0.0979))
ax1.annotate("", xy=(0.112,0.1), xytext=(0.124,0.1),arrowprops={'arrowstyle': '<->'},va='center')
ax1.annotate(textstr4, xy=(0.117, 0.101))
ax1.annotate("", xy=(0.1233,0.096), xytext=(0.1375, 0.096),arrowprops={'arrowstyle': '<->'},va='center')
ax1.annotate(textstr5, xy=(0.128, 0.0965))
ax1.annotate("", xy=(0.1375, 0.1), xytext=(0.151, 0.1),arrowprops={'arrowstyle': '<->'},va='center')
ax1.annotate(textstr6, xy=(0.142, 0.101))
ax1.annotate("", xy=(0.1508, 0.111), xytext=(0.165, 0.111),arrowprops={'arrowstyle': '<->'},va='center')
ax1.annotate(textstr7, xy=(0.156, 0.112))
ax1.legend(loc='lower right')
# ax1.text(0.02, .95, textfit, transform=ax1.transAxes, fontsize=12,
#         verticalalignment='top')
# ax1.set_xlim(E.min()-25,E.max()+25)

plt.savefig('calib.png')
#plt.show()
