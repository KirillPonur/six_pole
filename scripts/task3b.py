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


df=read(rec, sheet_name='Uотр=3В')
xlabel(r'$U_{\text{рез}}$, \text{В}',fontsize=16)
ylabel(r'$I$, деления',fontsize=16)
x,y=3*df['Uрез, В/3'],df['I, mA']
g = interpolate.interp1d(x,y, 'quadratic')
x=linspace(111,126,10)
y=g(x)
plot(x,y,'r')
plot(3*df['Uрез, В/3'],df['I, mA'],'ro',label=r'$U_\text{отр}=3$ В')
grid(which='major', linestyle='-')
grid(which='minor', linestyle=':')
minorticks_on()


df=read(rec, sheet_name='Uотр=19.5В')
x,y=3*df['Uрез, В/3'],df['I, mA']
g = interpolate.interp1d(x,y, 'quadratic')
x=linspace(min(x),max(x),1000)
y=g(x)
plot(x,y,color='darkblue')
plot(3*df['Uрез, В/3'],df['I, mA'],'v',label=r'$U_\text{отр}=19$ В',color='darkblue')

df=read(rec, sheet_name='Uотр=48В')
x,y=3*df['Uрез, В/3'],df['I, mA']
g = interpolate.interp1d(x,y, 'quadratic')
x=linspace(min(x),max(x),1000)
y=g(x)
plot(x,y,'g')
plot(3*df['Uрез, В/3'],df['I, mA'],'D',label=r'$U_\text{отр}=48$ В',color='green')
legend()
savefig(path.abspath('..'+'\\fig\\task3b.pdf'))
show()