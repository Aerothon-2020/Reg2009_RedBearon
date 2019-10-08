from __future__ import division # let 5/2 = 2.5 rather than 2
import numpy as npy
import pylab as pyl
from scalar.units import FT, SEC, LBF
from Aircraft_Models.Reg2009Aircraft_RedBearon.BoxWingAircraft.Aircraft import Aircraft
from Aircraft_Models.Reg2009Aircraft_RedBearon.BoxWingAircraft.BiWing import BoxWing

Vstl = npy.linspace(27,31,3)*FT/SEC
LLO  = npy.linspace(28,32,3)*LBF
Vplt = Vstl / (FT/SEC)

pyl.figure(1)
lgnd = []
for l in LLO:
    print("Calculating at LLO = ",l)
    vlo = []
    for v in Vstl:
        print("Calculating at Vstl = ",v)
        BoxWing.V_Stall = v
        BoxWing.Lift_LO = l
        Aircraft.TotalWeight = l
        
        vlo.append(Aircraft.GetV_LO() / (FT/SEC))
        
    pyl.plot(Vplt,vlo)
    lgnd.append('L_LO = %2.0f (lbf)' % (l/LBF)) 

pyl.title('Aircraft Lift of Velocity vs. Stall Velocity')
pyl.xlabel(r'$V_{stall}$ (ft/s)') ; pyl.ylabel(r'Aircraft $V_{LO}$ (ft/s)')
pyl.legend(lgnd, loc = 'best')

pyl.show()