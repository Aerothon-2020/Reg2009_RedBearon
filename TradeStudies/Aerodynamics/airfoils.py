from Aerothon.ACAirfoil import ACAirfoil
import pylab as pyl
from scalar.units import ARCDEG

af1 = ACAirfoil('e423')
af2 = ACAirfoil('S1223')
af3 = ACAirfoil('ch10sm')
af4 = ACAirfoil('fx74modsm')

#af1.PlotAirfoil(fig = 1, Alpha2d = 0*ARCDEG, subfig = 221)
#af2.PlotAirfoil(fig = 1, Alpha2d = 0*ARCDEG, subfig = 222)
#af3.PlotAirfoil(fig = 1, Alpha2d = 0*ARCDEG, subfig = 223)
#af4.PlotAirfoil(fig = 1, Alpha2d = 0*ARCDEG, subfig = 224)

af1.PlotAirfoil(fig = 1, Alpha2d = 0*ARCDEG, subfig = None, yo = 0.375, clr = 'g')
af2.PlotAirfoil(fig = 1, Alpha2d = 0*ARCDEG, subfig = None, yo = 0.125, clr = 'b')
af3.PlotAirfoil(fig = 1, Alpha2d = 0*ARCDEG, subfig = None, yo = -0.125, clr = 'm')
af4.PlotAirfoil(fig = 1, Alpha2d = 0*ARCDEG, subfig = None, yo = -0.375, clr = 'r')

#pyl.figure(1)
#pyl.subplot(221)
#pyl.title('Eppler 423 Airfoil')
#pyl.grid()
#
#pyl.subplot(222)
#pyl.title('Selig 1223 Airfoil')
#pyl.grid()
#
#pyl.subplot(223)
#pyl.title('Hollinger 10 smoothed Airfoil')
#pyl.grid()
#
#pyl.subplot(224)
#pyl.title('Modified Wortmann FX 74 Airfoil')
#pyl.grid()

pyl.show()