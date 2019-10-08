from __future__ import division # let 5/2 = 2.5 rather than 2
import numpy as npy
import pylab as pyl
from scalar.units import ARCDEG, FT, SEC, LBF
from scalar.units import AsUnit
from Aircraft_Models.Reg2009Aircraft_RedBearon.MonoWingAircraft.Aircraft import Aircraft


print 'Aircraft   V_LO     : ', AsUnit( Aircraft.GetV_LO(), 'ft/s')
print 'Wing       V_LO     : ', AsUnit( Aircraft.Wing.GetV_LO(), 'ft/s')
print 'Ground Roll Distance: ', AsUnit( Aircraft.Groundroll(), 'ft')

#
# Uncomment the next two lines and comment out the other "PlotPropulsionPerformance"
# call to plot for a range of values
#

WeightRange = npy.linspace(30,34,3)*LBF
Aircraft.PlotPropulsionPerformance(1, Vmax = 70*FT/SEC, TotalWeights = WeightRange)
ii = 2
for wt in WeightRange:
    Aircraft.TotalWeight=wt
    Aircraft.PlotLiftVelocityGroundroll(ii)
    ii += 1
    
Aircraft.Draw(ii+1)

pyl.show()