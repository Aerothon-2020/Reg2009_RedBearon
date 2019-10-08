from __future__ import division # let 5/2 = 2.5 rather than 2
from scalar.units import ARCDEG
from scalar.units import AsUnit
import numpy as npy
import pylab as pyl
from Aircraft_Models.Reg2009Aircraft_RedBearon.BoxWingAircraft.Aircraft import Aircraft

print 'Lift of Angle of Attack:', AsUnit( Aircraft.GetAlphaFus_LO(), 'deg' )
print 'Zero CM at Alpha       :', AsUnit( Aircraft.Alpha_Zero_CM, 'deg' )
print 'Horiz Design CL        :', Aircraft.GetHT_Design_CL()
print 'Horiz Incidence        :', AsUnit( Aircraft.HTail.i, 'deg' )

Aircraft.PlotTailLoad(fig=4)
Aircraft.PlotVTailLoad(fig=5)
Aircraft.PlotHTailLoad(fig=6)
Aircraft.HTail.Draw3DWingPolars(fig=3)
Aircraft.HTail.Draw2DAirfoilPolars(fig=2)
Aircraft.Draw(fig=1)
pyl.show()
