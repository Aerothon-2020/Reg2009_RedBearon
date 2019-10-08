from __future__ import division # let 5/2 = 2.5 rather than 2
import numpy as npy
import pylab as pyl
from scalar.units import FT, SEC, LBF, MIN, IN
from Aircraft_Models.Reg2009Aircraft_RedBearon.BoxWingAircraft.Aircraft import Aircraft

pyl.figure(1)

#
# Get the design point
#
dsgnGR = Aircraft.Groundroll() / (FT)
dsgnCR = Aircraft.Rate_of_Climb(1.07*Aircraft.GetV_LO()) / (FT/MIN)
pyl.plot([dsgnCR],[dsgnGR],'ro', markersize = 8)

gap = npy.linspace(0.25,0.4,4)
spn = npy.linspace(78,88,6)*IN

lgnd = ['Design']
arealist = []

grndroll = npy.zeros((len(gap),len(spn)))
clmbrate = npy.zeros((len(gap),len(spn)))

for ii in range(len(gap)):
    print "Calculating Gap = ",gap[ii]
    for jj in range(len(spn)):
        print "Calculating at Span = ",spn[jj]
        Aircraft.Wing.b = spn[jj]
        Aircraft.Wing.Gap = gap[ii]
        
        grndroll[ii][jj] = Aircraft.Groundroll() / (FT)
        clmbrate[ii][jj] = Aircraft.Rate_of_Climb(1.07*Aircraft.GetV_LO()) / (FT/MIN)
        
        print "   Wing Area = ",Aircraft.Wing.S / (IN**2)
        
for ii in range(len(gap)):
    clmplt = []
    grnplt = []
    for jj in range(len(spn)):
        clmplt.append(clmbrate[ii][jj])
        grnplt.append(grndroll[ii][jj])
        
    pyl.plot(clmplt,grnplt,ls = '--', lw = 2)        
    lgnd.append('Gap/Span = %3.2f' % (gap[ii]))
    
for jj in range(len(spn)):
    clmplt = []
    grnplt = []
    for ii in range(len(gap)):
        clmplt.append(clmbrate[ii][jj])
        grnplt.append(grndroll[ii][jj])
    
    pyl.plot(clmplt,grnplt, lw = 2)        
    lgnd.append('Span = %4.2f (in)' % (spn[jj]) / (IN))

pyl.axhline(y = 190, color = 'k')
pyl.axvline(x = 200, color = 'k')
pyl.title('Groundroll and Climb Rate for Varying Wing Span and Gap')
pyl.xlabel('Climb Rate (ft/min)') ; pyl.ylabel('Groundroll (ft)')
pyl.legend(lgnd, loc = 'best', numpoints=1, labelspacing = 0.0)

pyl.show()