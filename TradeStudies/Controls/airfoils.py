from Aerothon.ACAirfoil import ACAirfoil
import pylab as pyl

afv = ACAirfoil('/NACA0012/NACA0012.dat','NACA0012')
afh = ACAirfoil('clarky/clarky.dat','clarky')
afh.Inverted = True

afv.PlotAirfoil(1)
afh.PlotAirfoil(2)

pyl.figure(1)
pyl.title('Vertical Tail Airfoil')
pyl.grid()

pyl.figure(2)
pyl.title('Horizontal Tail Airfoil')
pyl.grid()

pyl.show()