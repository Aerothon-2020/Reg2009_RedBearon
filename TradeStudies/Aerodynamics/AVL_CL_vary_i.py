import numpy as npy
import pylab as pyl
from scalar.units import ARCDEG
from Aircraft_Models.Reg2009Aircraft_RedBearon.BoxWingAircraft.BiWing import BoxWing as biwing

ExecuteAVL = True

# Define the important parameters to vary
biwing.Gap        = 0.2
biwing.Stagger    = 0.0

# Find the CL based on the Aerothon and AVL models
Alpha1 = npy.linspace(-5,20,26)*ARCDEG
AlFuse = (biwing.AlphaFus(Alpha1)) / (ARCDEG)
Alpha2 = npy.linspace(0,24,9)
Incidence = npy.linspace(0,6,4)*ARCDEG

clrstr = 'bgrycmk'

ind = 0
legend = []
for i in Incidence:
    biwing.LowerWing.i = i
    CLAerothon = biwing.CL(Alpha1)
    CLAVL      = biwing.GetAVLCL(Alpha2,'i'+str(i), 'BiWing_trade_example/',ExecuteAVL)
    
    
    pyl.plot(AlFuse,CLAerothon,clrstr[ind])
    pyl.plot(Alpha2,CLAVL,clrstr[ind]+'s')
    ind = ind + 1
    
    legend.append('i = ' + str(i))
    
pyl.legend(legend, loc = 'lower right')
pyl.xlabel('Angle of Attack')

pyl.show()
pyl.ylabel('CL')
    

    