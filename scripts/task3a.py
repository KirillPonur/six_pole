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


df=read(rec, sheet_name='Uрез=90В')
xlabel(r'$U_{\text{отр}}$, \text{В}',fontsize=16)
ylabel(r'$I$, деления',fontsize=16)
plot(3*df['Uотр, В/3'],df['I, mA'],
		linestyle='-',
		marker='o',
		label=r'$U_{\text{рез}}=90$ В')
grid(which='major', linestyle='-')
grid(which='minor', linestyle=':')
minorticks_on()

df=read(rec, sheet_name='Uрез=96В')
plot(3*df['Uотр, В/3'],df['I, mA'],
	linestyle='-',
	marker='v',
	label=r'$U_{\text{рез}}=96$ В')


df=read(rec, sheet_name='Uрез=120В')
plot(3*df['Uотр, В/3'],df['I, mA'],
	linestyle='-',
	marker='D',
	label=r'$U_{\text{рез}}=120$ В')

legend()
savefig(path.abspath('..'+'\\fig\\task3a.pdf'))
show()