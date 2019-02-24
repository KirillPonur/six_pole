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


df=read(rec, sheet_name='Uрез=120В, Uотр=48В')
x=array(df['I,ma'])
y=array(df['I,дел'])
g = interpolate.interp1d(x,y, 'linear')
x=linspace(x[3],x[-1],1000)
y=g(x)
plot(x,y,color='red')
plot(df['I,ma'][2:],df['I,дел'][2:],'o',color='red',
	label=r'$U_{\text{отр}}=48 \text{ В}$')

df=read(rec, sheet_name='Uрез=12В, Uотр=19.5В')
x=array(df['I,ma'])
y=array(df['I,дел'])
g = interpolate.interp1d(x,y, 'cubic')
x=linspace(x[6],x[-2],1000)
y=g(x)
plot(x,y,color='darkblue')
plot(df['I,ma'][6:-1],df['I,дел'][6:-1],'o',color='darkblue',
	label=r'$U_{\text{отр}}=19.5 \text{ В}$')

df=read(rec, sheet_name='Uрез=12В, Uотр=3В')
x=array(df['I,ma'])
y=array(df['I,дел'])
g = interpolate.interp1d(x,y, 'cubic')
x=linspace(x[0],x[-1],1000)
y=g(x)
plot(x,y,color='green')
plot(df['I,ma'],df['I,дел'],'o',color='green',
	label=r'$U_{\text{отр}}=3 \text{ В}$')
x=array(df['I,ma'])
y=array(df['I,дел'])
xlabel(r'$I$, мА',fontsize=16)
ylabel(r'$I$, деления',fontsize=16)
grid(which='major', linestyle='-')
grid(which='minor', linestyle=':')    
minorticks_on()
legend()
savefig(path.abspath('..'+'\\fig\\task5.pdf'))
show()