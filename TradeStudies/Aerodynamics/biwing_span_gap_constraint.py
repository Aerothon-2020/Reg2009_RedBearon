import numpy as npy
import pylab as pyl
from scalar.units import ARCDEG, IN
from Aircraft_Models.Reg2009Aircraft_RedBearon.BoxWingAircraft.BiWing import BoxWing

#
# Set a constraint of the total length + height of the boxwing
# Using 2008 as a base:
#   -- height = biwing height + landing gear height
#   -- width  = wing span
#
LHconstraint = 100*IN   #constraint
landinggearH = 10*IN    #landing gear height

gapvals = npy.linspace(.1,.4,7)
alpha2d = npy.linspace(-5,20,26)*ARCDEG
a       = alpha2d / (ARCDEG)
#a       = BoxWing.AlphaWing(alpha2d) / (ARCDEG)

pyl.figure(1)
clrstr = 'bgrycmk'
ind = 0
labels=[]
for g in gapvals:
    BoxWing.Gap = g
    BoxWing.b   = (LHconstraint - landinggearH)/(1+g)
    CL         = BoxWing.CL(alpha2d)
    CDi        = BoxWing.CDi(alpha2d)
    CD         = BoxWing.CD(alpha2d)
    CDp        = CD - CDi
    print 'Gap = ', g,'    Oswald Efficiency = ', BoxWing.O_eff(), '    AR = ', BoxWing.AR
    
    pyl.subplot(131)
    pyl.plot(a,CL,clrstr[ind])
    
    pyl.subplot(132)
    pyl.plot(a,CD,clrstr[ind]+'-')
    pyl.plot(a,CDi,clrstr[ind]+'--')
    pyl.plot(a,CDp,clrstr[ind]+':')
    
    pyl.subplot(133)
    pyl.plot(a,CL/CD,clrstr[ind])
    ind = ind + 1
    labels.append('Gap = '+str(g))
    
pyl.subplot(131)
pyl.xlabel('alpha2d')
pyl.ylabel('CL')
pyl.legend(labels,loc='lower right')

pyl.subplot(132)
pyl.xlabel('alpha2d')
pyl.ylabel('CD (solid), CDi (dashed), CDp (dotted)')

pyl.subplot(133)
pyl.xlabel('alpha2d')
pyl.ylabel('CL/CD')
pyl.show()