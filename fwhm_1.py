##############################################################################
# PHYS 211 Python Example Scripts
# Example 4 - Least Squares Error
#
# PROGRAM:  This script reads in a typical spectrum file and fits a portion
#           of it to a Gaussian function using the least-squares technique.
# INPUT:    Example4_Data.tsv
# CREATED:  9/11/2014
# AUTHOR:   David McCowan [modified from work by William Irvine (2012),
#                         Frank Merrit (2013) and Michael Fedderke (2013)]
# MODIFIED: 07/27/2017 [Minor tweaks and updated to python3]
##############################################################################
import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize

# Read in the data from file using "loadtxt()".
# This time we have only x and y data (no uncertainties)
t, V, ch1,ch2 = np.loadtxt('/home/alemsolobog/Exper9/aj_data/day2_peaks', unpack=True, skiprows=1)

# In counting data such as this, we can assume our counts are Poisson-
# distributed and take the uncertainty to be dN = sqrt(N) for large N.
#  -For small N (say, N < 20), this is a slight underestimate, and as
#   N --> 0, this is totally wrong. (A dN = 0 means we know N = 0
#   exactly... always and forever, no ifs and or buts. This is incorrect.)
#  -To deal with N = 0, we use dN = 1.4 which represents the one-sided
#   68% confidence level upper limit. (For some justification, see
#   http://statpages.org/confint.html.)
dV = np.sqrt(np.abs(V))
for i, value in enumerate(dV):
    dV[i] = 0.0002

# Quickly plot the data to see what it looks like


# You should see one clear full energy peaks on the right.
# Let us fit the this peak to a Guassian function:
#   f(x) = N/sqrt(2pi) * exp[-(x-mu)^2/2sigma^2]
#  where p = [N, mu, sigma]
def fitfunc(p,x):
    return p[0]/(p[2]*np.sqrt(2*np.pi))*np.exp(-(x-p[1])**2/(2*p[2]**2)) + p[3] * x + p[4]
def residual(p, x, y, err):
    return (fitfunc(p, x)-y)/err

# For initial guesses, we can make some estimates from our plot above.
#   -The amplitude is about 3000 counts, so lets guess 50,000 counts total
#   -The center is near channel 375
#   -The width is about 50 channels, so sigma is about half that: 25
p0 = [0.02, 0.142, 0.005,-18, 2]

t2 = t[1260:1760]
V2 = V[1260:1760]
dV2 = dV[1260:1760]
print(min(t2),max(t2))
pf, cov, info, mesg, success = optimize.leastsq(residual, p0,
                               args=(t2, V2, dV2), full_output = 1)

if cov is None:
    print('Fit did not converge')
    print('Success code:', success)
    print(mesg)
else:
    print('Fit Converged')
    chisq = sum(info['fvec']*info['fvec'])
    dof = len(t2)-len(pf)
    pferr = [np.sqrt(np.abs(cov[i,i])) for i in range(len(pf))]
    print('Converged with chi-squared', chisq)
    print('Number of degrees of freedom, dof =',dof)
    print('Reduced chi-squared:', chisq/dof)
    print('Inital guess values:')
    print('  p0 =', p0)
    print('Best fit values:')
    print('  pf =', pf)
    print('Uncertainties in the best fit values:')
    print('  pferr =', pferr)
    print()

# Now let's plot the data and the fit at the same time to see how good
#  the fit turned out.
# We plot all the data in black, then replot the data used for the fit in red
    fig = plt.figure()
    ax = fig.add_subplot(111)
    #ax.plot(t, V, 'k.', label='Data')
    ax.plot(t2, V2, 'g.', label='Data in fit')

# We then plot the fit function. We could plot it at each point in "channel2"
#  and connect those points with straight lines. However, we may want a smoother
#  plot. To do so, we create a new array of points using "linspace()" that covers
#  the same range, but more densely. When we connect these points, the line will
#  be more smooth.

    T = np.linspace(min(t2), max(t2), 5000)
    ax.plot(T, fitfunc(pf, T), 'r',linewidth=3.0, label='Fit')
    ax.set_title('Absorption Spectrum of Rb Isotopes')
    ax.set_ylabel('Voltage, $V$ $(V)$')
    ax.set_xlabel('Time, $t$ $(sec)$')
    ax.legend()

    textfit = '$f(x) = N/\\sigma \\sqrt{2 \\pi} e^{-(x - \\mu)^{2}/2\\sigma^{2}}$ \n' \
              '$N = %.7f \pm %.7f$ $V$ \n' \
              '$\\mu = %.8f \pm %.8f$ \n' \
              '$\\sigma = %.8f \pm %.8f$ \n' \
              '$A = %.8f \pm %.8f$ \n' \
              '$B = %.8f \pm %.8f$ \n' \
              '$\chi^2= %.2f$ \n' \
              '$N = %i$ (dof) \n' \
              '$\chi^2/N = % .2f$' \
               % (pf[0], pferr[0], pf[1], pferr[1], pf[2], pferr[2],pf[3],pferr[3],pf[4],pferr[4],chisq, dof,
                  chisq/dof)
    ax.text(0.05, .95, textfit, transform=ax.transAxes, fontsize=12,
             verticalalignment='top')
    fit = fitfunc(pf,T)
    plt.savefig('rb85_f3.png')
    # for i in range(len(V2)):
    #     print(V2[i],fit[i])
