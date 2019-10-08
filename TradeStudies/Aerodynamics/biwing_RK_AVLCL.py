import numpy as npy
import pylab as pyl
from scalar.units import ARCDEG
from Aircraft_Models.Reg2009Aircraft_RedBearon.BoxWingAircraft.BiWing import BoxWing as biwing
from Aerocats2008BiWing import BoxWing as biwingAeroCats2008

ExecuteAVL = False

# Set up the variation of Oswald efficiency vs. gap
biwing.GapInterp  = [0.1,0.2,0.3,0.4]
biwing.OeffInterp = [1.1832,1.3371,1.4617,1.5676]

# Determine the correct Biwing correction factor for the given wing
#biwing.BWCFInterp     = [0.77,0.78,0.785,0.79]
biwing.BWCFInterp = [0.69,0.785,0.835,0.87]
biwing.LowerWing.FWCF = 1.0
biwing.UpperWing.FWCF = 1.0

# EndPlate
biwing.EndPlate.Fb      = [0.2,0.5,0.8]
biwing.EndPlate.TR      = [1,1,1]
biwing.EndPlate.Gam     = [0*ARCDEG,0*ARCDEG,0*ARCDEG]
biwing.EndPlate.Lam     = [0*ARCDEG,0*ARCDEG,0*ARCDEG]
#biwing.EndPlate.CEdge   = 'LE'


# Find the CL based on the Aerothon and AVL models
Alpha1 = npy.linspace(-5,20,26)*ARCDEG

biwing.Gap  = 0.1 
CLAerothon1 = biwing.CL(Alpha1)

biwing.Gap  = 0.2 
CLAerothon2 = biwing.CL(Alpha1)

biwing.Gap  = 0.3 
CLAerothon3 = biwing.CL(Alpha1)

biwing.Gap  = 0.4 
CLAerothon4 = biwing.CL(Alpha1)

CLAerocats2008 = biwingAeroCats2008.CL(Alpha1)

Alpha2 = npy.linspace(0,24,9)

biwing.Stagger = 0.0
biwing.Gap  = 0.1 
CLAVL1      = biwing.GetAVLCL(Alpha2,'g0.1', 'BiWing_trade_example/',ExecuteAVL)

biwing.Gap  = 0.2 
CLAVL2      = biwing.GetAVLCL(Alpha2,'g0.2', 'BiWing_trade_example/',ExecuteAVL)

biwing.Gap  = 0.3 
CLAVL3      = biwing.GetAVLCL(Alpha2,'g0.3', 'BiWing_trade_example/',ExecuteAVL)

biwing.Gap  = 0.4 
CLAVL4      = biwing.GetAVLCL(Alpha2,'g0.4', 'BiWing_trade_example/',ExecuteAVL)

AlWing = biwing.AlphaWing(Alpha1)
AlWing = AlWing / (ARCDEG)
Alpha1 = Alpha1 / (ARCDEG)

pyl.figure(1)
pyl.plot(AlWing,CLAerothon1,'y-')
pyl.plot(AlWing,CLAerothon2,'b-')
pyl.plot(AlWing,CLAerothon3,'g-')
pyl.plot(AlWing,CLAerothon4,'r-')
pyl.plot(AlWing,CLAerocats2008,'k-')
pyl.plot(Alpha2,CLAVL1,'ys')
pyl.plot(Alpha2,CLAVL2,'bs')
pyl.plot(Alpha2,CLAVL3,'gs')
pyl.plot(Alpha2,CLAVL4,'rs')

label = ['Aerothon CL G=0.1','Aerothon CL G=0.2','Aerothon CL G=0.3','Aerothon CL G=0.4','Aerocats 2008 CL G=0.2']
label.append('AVL: G=0.1, S=0, square')
label.append('AVL: G=0.2, S=0, square')
label.append('AVL: G=0.3, S=0, square')
label.append('AVL: G=0.4, S=0, square')

#pyl.legend(['2DCL (2d alpha)','2DCL (2d alpha+avg downwash)','2DCL (2d alpha+sum downwash)',lb1,lb2,lb3,lb4,lb5,lb6,lb7,lb8,lb9,lb10], loc = 'lower right')
pyl.legend(label, loc = 'lower right')

pyl.show()

