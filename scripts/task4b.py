from pylab import *
from matplotlib import rc
from functions import parsing
import os.path as path
import sys
from scipy import interpolate
from pandas import read_excel as read
rc('text', usetex=True)
rc('text.latex', preamble=[r'\usepackage[russian]{babel}',
                         r'\usepackage{amsmath}',
                        r'\usepackage{amssymb}'])


rc('font', family='serif')

rec = path.abspath('..'+'\\rec\\rec.xlsx')


# df=read(rec, sheet_name='Uотр=3В')
# plot(3*df['Uрез, В/3'],df['lambda, cm'],'v',label=r'$U_{\text{отр}}=3$ В')

df=read(rec, sheet_name='Uотр=19.5В')
plot(3*df['Uрез, В/3'],df['lambda, cm'],'o',label=r'$U_{\text{отр}}=19$ В')
ylim((10.4,10.65))
xlabel(r'$U_{\text{отр}}$, \text{В}',fontsize=16)
ylabel(r'$\lambda$, см',fontsize=16 )
grid(which='major', linestyle='-')
grid(which='minor', linestyle=':')
minorticks_on()

df=read(rec, sheet_name='Uотр=48В')
plot(3*df['Uрез, В/3'],df['lambda, cm'],'v',label=r'$U_{\text{отр}}=48$ В')
legend()
savefig(path.abspath('..'+'\\fig\\task4b.pdf'))
show()