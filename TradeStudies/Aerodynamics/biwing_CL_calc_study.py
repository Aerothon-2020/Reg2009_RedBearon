from __future__ import division # let 5/2 = 2.5 rather than 2
from scalar.units import M, FT, IN, ARCDEG, RAD, LBF, SEC, KG
import numpy as npy
import pylab as pyl
from Aircraft_Models.Reg2009Aircraft_RedBearon.BoxWingAircraft.BiWing import BoxWing

BoxWing.Stagger = 0.0
BoxWing.Gap = 0.2
b = BoxWing.b
c = BoxWing.MAC()

stgvals = npy.linspace(-1,1,5)
gapvals = npy.linspace(.1,.4,7)
#alpha2d = npy.linspace(-5,20,26)*ARCDEG
#a       = alpha2d / (ARCDEG)

pyl.figure(1)
clrstr = 'bgrycmk'
ind = 0
labels=[]
for s in stgvals:
    CL2_CL3 = []
    CL2_CL1 = []
    for g in gapvals:
        BoxWing.Stagger = s
        BoxWing.Gap     = g
        
        alpha2d=0*ARCDEG
        cl1 = BoxWing.CL(alpha2d)
        cl2 = BoxWing.CL2(alpha2d)
        cl3 = (BoxWing.UpperWing.CL(alpha2d) + BoxWing.LowerWing.CL(alpha2d))/2
        CL2_CL1.append(cl2/cl1)
        CL2_CL3.append(cl2/cl3)
    
    pyl.subplot(121)
    pyl.plot(gapvals,CL2_CL3,clrstr[ind])
    
    pyl.subplot(122)
    pyl.plot(gapvals,CL2_CL1,clrstr[ind])
    
    ind = ind + 1
    labels.append('Stagger = '+str(s))

pyl.subplot(121)
pyl.xlabel('Gap/Span')
pyl.ylabel('Altman CL / Uncorrected CL  (% diff)')
pyl.legend(labels,loc='lower right')

pyl.subplot(122)
pyl.xlabel('Gap/Span')
pyl.ylabel('Altman CL / AVL CL  (% diff)')
pyl.legend(labels,loc='lower right')

pyl.show()